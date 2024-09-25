import json
import datetime

import pandas as pd
import numpy as np

from flask import Flask, render_template, request, redirect
from flask_babel import Babel, gettext as _, refresh

from werkzeug.middleware.proxy_fix import ProxyFix

import datasrc

language = 'en'
app = Flask(__name__,static_folder='LogEval/static',static_url_path='/LogEval/static')
app.wsgi_app = ProxyFix(app.wsgi_app)
babel = Babel(app=app)
babel.init_app(app, locale_selector=lambda: language)

old_route = app.route
app.route = lambda r,*args,**kw: old_route(f'/LogEval/{r}', *args, **kw)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/news")
def news():
    return render_template("news.html", news=datasrc.get_news())


@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/example")
def example():
    return render_template("example.html")

@app.route("/submitting", methods=['POST'])
def submitting():
    pd.DataFrame({k: [v] for k,v in request.json.items()}).to_csv("submitted.csv",index=False,header=False,mode='a')
    return "success"


statistics_order = None


@app.route("/leaderboard")
def leaderboard():
    global statistics_order
    statistics_order = None
    return render_template("leaderboard.html")


@app.route("/chg_order", methods=['POST'])
def chg_order():
    global statistics_order
    statistics_order = request.json
    return "success"


def toNumber(x: pd.Series):
    a = x.values
    return a[-1] if a.shape[0]>=0 else pd.NA


@app.route("/statistics", methods=['POST'])
def statistics():
    stc = datasrc.get_statistics()
    updatetime = stc["updatetime"]
    leaderbrd = stc["leaderboard"]
    leaderbrd = leaderbrd.loc[
        (leaderbrd["task"] == {
            "parsing": "Log Parsing",
            "abnormal": "Log Anomaly Detection",
            "summary": "Log Summary",
            "diagnose": "Log Fault Diagnosis"
        }[request.json["task"]]) &
        (leaderbrd["side"] == {
            "nativeQA": "naive Q&A",
            "scQA": "SC Q&A"
        }[request.json["side"]]) &
        (leaderbrd["instr"] == {
            "zeroshot": "zero-shot",
            "fewshot": "few-shot"
        }[request.json["instr"]])
        ]
    modelList = leaderbrd["model"].unique()
    leaderbrd = pd.DataFrame({
        "model": modelList,
        "Chinese accuracy": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "Chinese") &
                                 (leaderbrd["measure"] == "accuracy")
                                 , "value"]) for i in modelList],
        "Chinese non-accuracy": [toNumber(leaderbrd.loc[
                                     (leaderbrd["model"] == i) &
                                     (leaderbrd["lang"] == "Chinese") &
                                     (leaderbrd["measure"] != "accuracy")
                                     , "value"]) for i in modelList],
        "English accuracy": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "English") &
                                 (leaderbrd["measure"] == "accuracy")
                                 , "value"]) for i in modelList],
        "English non-accuracy": [toNumber(leaderbrd.loc[
                                     (leaderbrd["model"] == i) &
                                     (leaderbrd["lang"] == "English") &
                                     (leaderbrd["measure"] != "accuracy")
                                     , "value"]) for i in modelList],
    }) if request.json["side"] == "nativeQA" else pd.DataFrame({
        "model": modelList,
        "Chinese accuracy": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "Chinese") &
                                 (leaderbrd["measure"] == "accuracy")
                                 , "value"]) for i in modelList],
        "Chinese f1-score": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "Chinese") &
                                 (leaderbrd["measure"] == "F1-score")
                                 , "value"]) for i in modelList],
        "Chinese f1-var": [toNumber(leaderbrd.loc[
                               (leaderbrd["model"] == i) &
                               (leaderbrd["lang"] == "Chinese") &
                               (leaderbrd["measure"] == "F1-score Variance")
                               , "value"]) for i in modelList],
        "English accuracy": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "English") &
                                 (leaderbrd["measure"] == "accuracy")
                                 , "value"]) for i in modelList],

        "English f1-score": [toNumber(leaderbrd.loc[
                                 (leaderbrd["model"] == i) &
                                 (leaderbrd["lang"] == "English") &
                                 (leaderbrd["measure"] == "F1-score")
                                 , "value"]) for i in modelList],
        "English f1-var": [toNumber(leaderbrd.loc[
                               (leaderbrd["model"] == i) &
                               (leaderbrd["lang"] == "English") &
                               (leaderbrd["measure"] == "F1-score Variance")
                               , "value"]) for i in modelList],
    })
    global statistics_order
    if statistics_order not in list(leaderbrd.columns)\
            and statistics_order not in {'Chinese edit-dis', 'English edit-dis'}:
        statistics_order = None
    if statistics_order:
        if statistics_order in {'Chinese edit-dis', 'English edit-dis'}:
            leaderbrd.sort_values(by=statistics_order.replace('edit-dis', 'non-accuracy'), inplace=True)
        else:
            leaderbrd.sort_values(by=statistics_order, ascending=(statistics_order == 'model'), inplace=True)
    leaderbrd = '\n'.join(
        [f"<tr> {''.join([f'<td> {leaderbrd.loc[i, j]} </td>' for j in leaderbrd.columns])} </tr>" for i in leaderbrd.index])
    return json.dumps({'updatetime': updatetime.strftime('%Y-%m-%d %H:%M'), 'leaderboard': leaderbrd})


@app.route("/blank")
def blank():
    return render_template("blank.html")


@app.route("/lang_change")
def lang_change():
    global language
    if language == 'zh_CN':
        language = 'en'
    else:
        language = 'zh_CN'
    refresh()
    return redirect(request.referrer)

from flask import Flask, render_template, request
from janome.tokenizer import Tokenizer as JanomeTokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary_result = ""
    if request.method == "POST":
        text = request.form["text"]

        # 文単位で分割（簡易的に "。" で区切る）
        sentences = text.replace("。\n", "。").split("。")
        preprocessed_text = "。\n".join([s.strip() for s in sentences if s.strip() != ""]) + "。"

        parser = PlaintextParser.from_string(preprocessed_text, Tokenizer("japanese"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, 2)

        summary_result = "\n".join(["- " + str(sentence) for sentence in summary])

    return render_template("index.html", summary=summary_result)

if __name__ == "__main__":
    app.run()

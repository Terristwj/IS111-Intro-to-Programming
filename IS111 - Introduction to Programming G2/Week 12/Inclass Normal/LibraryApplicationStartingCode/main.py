from flask import Flask, render_template, request, abort
import config as cfg
import model as md
import util

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        criterion_index = request.form['criterion_index']
    else:
        criterion_index='0'
    
    print(criterion_index)
    item_list = md.get_sorted_items(cfg.item_list, int(criterion_index))
    return render_template("index.html", object_list=item_list, criteria=cfg.criterion_list, last_criterion_index=criterion_index)

@app.route("/<input_str>/")
def detail(input_str):
    input_str = input_str.strip()
    words = input_str.split()
    input_str = ' '.join(words)
    
    if input_str.startswith('lib_'):
        input_str = input_str[4:]
        item_list = util.read_items_of_given_library_from_file(cfg.item_file_name, input_str)
        return render_template("library.html", library_name=input_str, object_list=item_list)
    elif input_str.startswith('item_'):
        input_str = input_str[5:]
        loan_list = cfg.loan_dict[input_str]
        return render_template("item_loans.html", title=input_str, loan_list=loan_list)
    else:
        abort(404)

@app.route("/statistics")
def statistics():
    (ids, graphJSON) = md.generate_graphs(cfg.item_file_name, cfg.loan_file_name)
    return render_template("statistics.html", ids=ids, graphJSON=graphJSON)
        
if __name__ == "__main__":
    cfg.item_list = util.read_items_from_file(cfg.item_file_name)
    cfg.loan_dict = util.read_loans_from_file_to_dict(cfg.loan_file_name)
    app.run(port=5004, debug = True)
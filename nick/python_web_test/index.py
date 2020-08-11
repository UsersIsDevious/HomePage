from browser import document, alert,html,ajax

def echo(event):
	rslt = document["result"]
	if document["zone"].value == "0505keitan":
		alert('本当に'+document["zone"].value+'でいいですか')
		rslt <= html.H1("お前恐ろしいお文字列打つな.....怖")
	else:
		alert(document["zone"].value+'が入力されています')
		rslt.text = document["zone"].value
def addition(event):
	data_out = document["AdditionResponse"]
	data_1 = document["data_1"].value
	data_2 = document["data_2"].value
	if  data_1.isnumeric() and data_2.isnumeric():
		data_out.text = str(int(data_1) + int(data_2))
	else:
		data_out.text = "数字として認識できないか数字以外が含まれています"
def ajax_test():
	alert(ajax.ajax().open("GET", "https://www.yahoo.co.jp", True).send().responseText)

document["mybutton"].bind("click", echo)
document["AdditionOn"].bind("click", addition)
document["ajax_test"].bind("click", ajax_test)
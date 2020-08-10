from browser import document, alert

def echo(event):
	rslt = document["result"]
	if document["zone"].value == "0505keitan":
		alert('本当に'+document["zone"].value+'でいいですか')
		rslt = "<h1>お前恐ろしいお文字列打つな.....怖</h1>"
	else:
		alert(document["zone"].value+'が入力されています')
		rslt.text = document["zone"].value
document["mybutton"].bind("click", echo)
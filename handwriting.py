import pywhatkit as pw

text="My name is Vaibhav Negi . I am from Moradabad,Uttar Pradesh . Right now, I am pursuing B.Tech from Moradabad Institute of Technology, " \
",AKTU. My aim is to be a good IoT engineer in BIG company working on real world live projects!"

pw.text_to_handwriting(text,"demo.png",[0,0,200])

print("Thank you , text is converted !")
import frida, sys

def on_message(message, data):
    if message['type']== 'send':
        print("[*]{0}".format(message['payload']))
    else:
        print(message)

jscode ="""

Java.perform(function(){
     //obtain reference of the activity currently running
     var mainActivity = Java.use("sg.vantagepoint.a.c");
     //obtain reference of the function which needs to be called
     mainActivity.a.implementation = function (){

     console.log("Inside function a ");
     return false;
     };

     mainActivity.b.implementation = function (){

     console.log("Inside function c ");
     return false;
     };

     mainActivity.c.implementation = function (){

     console.log("Inside function c ");
     return false;
     };
});
"""

process = frida.get_usb_device(1).attach('owasp.mstg.uncrackable1')
script = process.create_script(jscode)
script.on('message',on_message)
script.load()
sys.stdin.read()

     

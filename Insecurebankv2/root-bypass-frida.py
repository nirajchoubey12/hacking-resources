import frida, time

def on_message(message, data):
    if message['type'] == 'send':
        print("[*]{0}".format(message['payload']))
    else:
        print(message)
        print('error')

device = frida.get_usb_device(1)

pid = device.spawn("com.android.insecurebankv2") # you can use attach as well

device.resume(pid)

time.sleep(1) # without it Java.perform silently fails
session = device.attach(pid)

script = session.create_script(open("root-bypass-frida.js").read())

script.on('message',on_message)
script.load()

# prevent the python script from terminating
input()

#python root-bypass-frida.py

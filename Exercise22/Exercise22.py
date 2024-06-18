garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

reversed_garbled = garbled[::-1]

message = ''.join(filter(lambda x: x != 'X' ,reversed_garbled))

print (message)

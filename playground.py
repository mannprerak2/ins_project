from stegano import lsb

secret = lsb.hide("./data/img.png", "hello world")
secret.save("./output.png")

message = lsb.reveal("./output.png")
print(message)

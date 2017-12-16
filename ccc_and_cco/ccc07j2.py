while True:
  a = input()
  if a == "TTYL":
    print("talk to you later")
    break
  else:
    print(a
      .replace("CU", "see you")
      .replace(":-)", "I'm happy")
      .replace(":-(", "I'm unhappy")
      .replace(";-)", "wink")
      .replace(":-P", "stick out my tongue")
      .replace("(~.~)", "sleepy")
      .replace("TA", "totally awesome")
      .replace("CCC", "Canadian Computing Competition")
      .replace("CUZ", "because")
      .replace("TY", "thank-you")
      .replace("YW", "you're welcome")
    )

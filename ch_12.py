
def most_frequent(evalStr):
  letter_hist = make_hist(evalStr)
  print(letter_hist)

  t=[]
  for x, freq in letter_hist.items():
    t.append( (freq, x) )

  t.sort(reverse=True)

  res=[]

  for freq, x in t:
    res.append(x)

  print(t)
  print(res)

def make_hist(evalStr):
  hist = {}
  hist = dict()
  for c in evalStr.lower():
    if c not in hist:
      hist[c] = 1
    else:
      hist[c] += 1

  return hist


evalStr = "The lazy brown dog jumped over the quick brown fox. Then the fox hid in the bush."
most_frequent(evalStr)

import json
import jsonlines

data = "eli5"
#pred_f = "/data/junhahyung/DPR/outputs/2023-01-04/15-25-34/d_qa_nq_result.json"
#pred_f = "/data/junhahyung/DPR/outputs/2023-01-04/16-03-17/d_qa_hotpotqa_result.json"
pred_f = "/data/junhahyung/DPR/outputs/2023-01-04/16-03-25/d_qa_eli5_result.json"
#pred_f = "/data/junhahyung/DPR/outputs/2023-01-04/16-02-54/d_qa_trivia_result.json"
kilt = f"/data/junhahyung/contextualized_GENRE/dataset/total_qa/{data}-test_without_answers-kilt.jsonl"

query2id = {}
with jsonlines.open(kilt) as f:
   for elem in f.iter():
      query2id[elem["input"]] = elem["id"]

title2id = json.load(open("/data/junhahyung/contextualized_GENRE/dataset/kilt_title2id.json"))

ret = []
f = json.load(open(pred_f))
for elem in f:
   q = elem["question"]
   if data == "eli5":
      if q == "Why doesn't water in a pond just soak into the ground?":
         qid = "bjhv4i"
      elif q == "Venezuelan currency has inflated to over 1,000,000 times its value. Why can't they just reassign a value to their dollar to fix the problem?":
         qid = "98uhoi"
      elif q == "How do those websites where you take surveys to earn money work? Why do they pay you for answering questions and how legit is it? Cause I'm seriously considering it to earn some on the side and don't wanna get into anything dodgy":
         qid = "a0p9o8"
      elif q == "Italy's antitrust authority is investigating Google for alleged abuse of dominant market position. Why is this a problem if Google is everyone's go to(for the most part)?":
         qid = "bpnr8p"
      elif q == "Why the initiatives against straws but not the plastic cups and lids they come in? Shouldn't they tackle the “bigger” problem?":
         qid = "cnl4hu"
      elif q == "Was the idea that “freedom of speech doesn't mean freedom from [societal] consequences” ever a point of confusion in the first place?":
         qid = "cvrgdu"
      elif q == "what does a neurologist do that's different than a psychiatrist?":
         qid = "bfj6wy"
      elif "Why don't any other seeds" in q:
         qid = "9zuvlw"
      elif "When we're scared of something, why does the brain make you think about it" in q:
         qid = "bbyly1"
      elif "If there are an infinite number of universes, wouldn't there be one where a machine was" in q:
         qid = "2c1hi8"
      elif "Bertrand Russell's analogy of a teapot to explain" in q:
         qid = "95137y"
      elif "why can people who aren't able to see properly IRL, see in VR?" in q:
         qid = "c88g98"
      elif "If the human body uses fever to kill infections, why can't a limb be heated up" in q:
         qid = "bt1w39"
      elif "Why don't structure fires create a chain reaction of gas line explosions the lead back all the way" in q:
         qid = "cwj5ui"
      elif "Can someone explain the science to me of what exactly about an atomic bomb makes it so powerful" in q:
         qid = "afg69c"
      elif "why didn't anyone bother to object Hitler breaking the Enabling Act?" in q:
         qid = "b17vg0"
      elif "Why can't there be solar panels for different EM waves?" in q:
         qid = "c7shnr"
      elif "since movie scenes aren't filmed chronologically, how do filmmakers" in q:
         qid = "bv1a6i"
      elif "What causes us to randomly think about people or things from many years ago" in q:
         qid = "bz41z1"
      elif "Why do streaming services (Netflix," in q:
         qid = "9z7y6b"
      elif "What is QAnon and why are it" in q:
         qid = "95caqc"
      elif "why does your bum hurt/rash if you don't wipe properly? Is there something in faeces which reacts to your skin," in q:
         qid = "b0jr2k"
      elif "Why isn't authors collaborating on fiction books common?" in q:
         qid = "bx1taj"
      elif "Why don't we see devices use B, C" in q:
         qid = "bvy0p6"
      elif "why can't we make food through chemical processes instead for planting" in q:
         qid = "bijlvn"
      elif "investing money in a company why is there risk involved? surely" in q:
         qid = "9xuqsk"
      elif "Why is The Beatles' Sergeant" in q:
         qid = "9ym66n"
      elif "Why do tech companies like Twitter and Google need so many software" in q:
         qid = "auo2rb"
      elif "what exactly is the brain doing" in q:
         qid = "apj4sy"
      elif "is there a mathematical theory that" in q:
         qid = "a4ftky"
      elif "Does streaming a YouTube video use the same amount of data" in q:
         qid = "ah4epn"
      elif "preventing companies from putting something along the lines" in q:
         qid = "bv0wkm"
      elif "How exactly did James Cordier and" in q:
         qid = "9ywsif"
      elif "How do my eyes automatically close when" in q:
         qid = "a92xcc"
      elif "payment only windows added / built in to" in q:
         qid = "9ugddu"
      elif "Why is it that the wooden tray we use to cook" in q:
         qid = "ar0yfu"
      elif "Why does it cost millions of dollars for the US Government to do certain things" in q:
         qid = "9yzvsx"
      elif "Why wouldn't flushing my sinuses out with Listerine" in q:
         qid = "bnz4gu"
      elif "Why don't we use tomato leaves as herbs, they're" in q:
         qid = "95exh9"
      elif "main facial characteristic that allows us to identify" in q:
         qid = "ah6qv8"
      elif "When hunting for fish, Polar Bears cover up their black noses making them" in q:
         qid = "b061fh"
      elif "There's millions if not billions of creatures in the ocean" in q:
         qid = "cb0jr5"
      elif "What does it mean to purge voters. As a Canadian" in q:
         qid = "9prxgo"
      elif "why does your skin bubble when it gets" in q:
         qid = "bu7zpe"
      elif "How does one small meteor like say the size of" in q:
         qid = "9muxmw"
      elif "why get a loan for anything if you're going to pay" in q:
         qid = "a7ycqp"
      elif "Why can't observatories be built in the ocean away" in q:
         qid = "cly5o8"
      elif "I know it's from repetitive damage over time" in q:
         qid = "c6i1e6"
      elif "Why doesn't the runners high damage the body in the same" in q:
         qid = "bsvuxq"
      elif "if air is a mixture of elements" in q:
         qid = "a793v9"
      elif "Why can't the Super Bowl be moved to a Saturday" in q:
         qid = "amlt1v"
      elif "People often say that" in q:
         qid = "b8raau"
      elif "what is QAnon and why are" in q:
         qid = "95caqc"
      else:
         try:   
            qid = query2id[q]
         except:
            print(q) 

   elif data == "nq":
      if q == "what are the 6 elements that cycle through earth's natural systems in different forms":
         qid = "500946051418147664"
      elif q == "who is considered one of america's first significant film composers of the early twentieth century":
         qid = "-2728126306690976067"
      else:
         qid = query2id[q]
   elif data == "hotpotqa":
      if q == "Which magazine has a wider scope, New York Woman or Femmes d'Aujourd'hui?":
         qid = "5ab223c6554299722f9b4cc3"
      elif q == "Which women's magazine was founded first, Woman's Viewpoint or Femmes d'Aujourd'hui?":
         qid = "5a74587e55429974ef308bdf"
      else:
         qid = query2id[q]
   elif data == "triviaqa":
      if "on what Washington DC thoroughfare is the White House located?" in q:
         qid = "qg_3267"
      elif "Which European boyband released a 2000 album" in q:
         qid = "qb_4420"
      elif "US Department of Defense history of the United States political-" in q:
         qid = "qb_4398"
      elif "Who played Mary Goodnight in the 1974 James Bond film" in q:
         qid = "qb_4164"
      elif "the slogan for which car manufacturer?" in q:
         qid = "qb_4146"
      elif "is a book written by which member of The Beatles?" in q:
         qid = "qb_4051"
      elif "What is former England footballer Gary Lineker's middle name?" in q:
         qid = "qb_4024"
      else:
         qid = query2id[q]
   else:
      try:
         qid = query2id[q]
      except:
         print(f"Missing {q}")
         continue
   ctxs = elem["ctxs"]
   _provenance_list = []
   for ctx in ctxs[:10]:
      try:
         _id = title2id[ctx["title"]]
      except:
         continue
      _provenance_list.append({"wikipedia_id": int(_id)})
   ret.append({"id": str(qid), "output": [{"answer": "", "provenance": _provenance_list}]})
    
assert len(ret) == len(query2id), f"Official: {len(query2id)} // Pred: {len(ret)}"

with open(f"{data}_test.pred.jsonl", "w", encoding='utf-8') as f:
   for elem in ret:
      json.dump(elem, f)
      f.write("\n")

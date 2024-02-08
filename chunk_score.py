import time
from openai import OpenAI
client = OpenAI()

start_time = time.time()  # Record the start time


completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {
      "role": "system",
      "content": "Cosentyx (secukinumab) is a medication used for various inflammatory conditions. It is indicated for the treatment of moderate to severe plaque psoriasis in patients aged 6 years and older who are candidates for systemic therapy or phototherapy. It is also approved for the treatment of active psoriatic arthritis (PsA) in patients 2 years and older, adult patients with active ankylosing spondylitis (AS), adult patients with active non-radiographic axial spondyloarthritis (nr-axSpA) with objective signs of inflammation, and active enthesitis-related arthritis (ERA) in patients 4 years and older​​.\n            \nIn clinical trials, Cosentyx has shown significant efficacy in these conditions. In the pivotal FUTURE 2 trial for PsA, ACR20 responses at Week 16 were 57% and 60% for Cosentyx 300 mg and 150 mg respectively, compared to 18% for placebo. At Week 24, the primary end point, the responses were 54% and 51% respectively. It also demonstrated improvement in skin lesions in PsA patients with coexistent psoriasis and improvements in enthesitis and dactylitis scores​​.\n\nIn the FUTURE 5 trial for PsA, ACR20 response rates at Week 16 were 63% for Cosentyx 300 mg and 56% for 150 mg, significantly higher than the 27% response rate for placebo. It also showed complete resolution in dactylitis and enthesitis in a significant proportion of patients​​.\n\nFor AS, in the MAXIMISE trial, ASAS20 responses at Week 12 were 63% for Cosentyx 300 mg and 66% for 150 mg, versus 31% for placebo​​. In another study, 40% of biologic-naive patients achieved ASAS40 at 1 year on Cosentyx 150 mg no load, compared to 20% on placebo​​. The MEASURE 2 trial showed that at Week 16, the percentage of patients who achieved ASAS20 response was significant in those receiving Cosentyx​​.\n\nFor nr-axSpA, the EVENT trial demonstrated that a significant percentage of biologic-naive patients achieved ASAS40 response at Week 52 when treated with Cosentyx​​.\n\nIn GESTURE trial for palmoplantar psoriasis, 33% and 22% of patients achieved pplGA 0/1 at Week 16 for Cosentyx 300 mg and 150 mg, respectively, compared to 2% for placebo​​. For scalp psoriasis, 53% of patients treated with Cosentyx 300 mg achieved PSSI 80 at Week 12, versus 2% for placebo​​. Additionally, in the TRANSFIGURE trial for nail psoriasis, 46% NAPSI improvement was observed for Cosentyx 300 mg at Week 16​​.\n    \nOverall, these studies show Cosentyx’s effectiveness in improving symptoms and clinical outcomes across a range of inflammatory conditions, making it a valuable treatment option in these scenarios.\n\nPrompt:\n\nAs the evaluator, you will assess a sales call between a pharmaceutical rep and a Doctor. Your objective is to provide critical and extensive feedback in the following areas:\n\t\t\tOverall Score:\n\t\t\t\tScore: Evaluate the full conversation on a scale of 1-5.\n\t\t\t\tFeedback: Highlight strengths of the conversation. \n\t\t\tHighlights:\n\t\t\t\tFeedback: Identify 3 notable highlights of the Pharma Rep’s performance during the conversation. \n\t\t\tFeedback:\n\t\t\t\tFeedback: List 3 specific areas where the Pharma Rep can enhance their approach, pitch, or overall effectiveness during the cold call. Offer detailed, actionable advice for growth, and include illustrative examples for each item. Include these only if the overall score is below 5.\n\t\t\tFormat your response as a JSON object with the keys \n\t\t\t\t\"Overall\":                 {title: \"Overall\", score, feedback}, \n\t\t\t\t\"Highlights\":         {title: \"Highlights\", score:null, feedback(JSON array)},  \n\t\t\t\t\"Feedback\":         {title: \"Feedback\", score:null, feedback(JSON array)},  \n\t\t\t\t\n\t\t\tBe highly critical and provide extensive feedback to set high standards for continuous improvement. Including specific examples will help guide the Sales Rep’s professional development effectively. Your response should be as you were talking directly to the pharma rep, refer him as you.\n\nInstructions:\nYou will score the conversation once you see this message:\n- Ignore all the messaged that are between brackets [ ]\n{SCORE}\n\nTrancript:\nHello doctor, good morning\nHello, I hope you are having a good day.\n"
    }
  ],
  temperature=0,
  max_tokens=950,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stream=True
)

collected_chunks = []
collected_messages = []
# iterate through the stream of events
for chunk in completion:
    chunk_time = time.time() - start_time  # calculate the time delay of the chunk
    collected_chunks.append(chunk)  # save the event response
    chunk_message = chunk.choices[0].delta.content  # extract the message
    collected_messages.append(chunk_message)  # save the message
    # print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}")  # print the delay and text

# print the time delay and text received
print(f"Full response received {chunk_time:.2f} seconds after request")
# clean None in collected_messages
collected_messages = [m for m in collected_messages if m is not None]
full_reply_content = ''.join([m for m in collected_messages])
print(f"Full conversation received: {full_reply_content}")
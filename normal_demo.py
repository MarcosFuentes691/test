import time
from openai import OpenAI
client = OpenAI()

start_time = time.time()  # Record the start time

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be roleplaying as an avatar.\n\nFollow the given script.\n\nScript:\nJohn\nHey avatar- I’m John.  Great to meet and thanks for making some time for us today, I’m excited for the chat.  If you’re alright with it, perhaps a great place to start might be to learn a bit about your interest in Quantified- and what you’re looking to solve for?\n\nAvatar\nHey John- sounds like a plan.  My name is Avatar and I’m the Senior Director of Global Sales Enablement for blah,blah company.  I have a team of 4 that report to me, and we’re responsible for all of blah,blah’s sales training and enablement activities.  The reason I reached out, is that we’re currently certifying all of our sellers in a number of areas- discovery, positioning, and product knowledge to name a few.  Right now, my team of 4, along with some of our sales leaders are the ones who are conducting these certification sessions.  We’re doing these manually, and there’s no way we can keep this up.  Certainly not with any growth.  Your solution looked like it might help us scale our certifications a bit better.\n\nJohn\nThanks- very helpful, and I appreciate the background.  So when you say you’re not likely to be able to keep it up, what are some of the specific challenges you’re experiencing?  Is it just pulling your team and the sales leaders in too many different directions?  Or perhaps just painful to coordinate times for all of these sessions?\n\nAvatar\nYeah- definitely a bit of both.  It’s like pulling teeth to get my sales leaders to help out here.  They all genuinely want for our sellers to perform at a high level, and to have command of their messaging.  But if we’re being honest- they need to be out supporting deals, and not doing a bunch of role play certifications.  Even under the best of circumstances though- scheduling these role play sessions across the organization is an absolute nightmare.  Another problem I have is that some of these certifications have just become a box-checking exercise.  Even just on my team, some folks will hold our sellers to a higher standard than others.  Some are better at conducting the role play than others.  A number of things we’re doing that really could benefit from some standardization.\n\nJohn\nWell it’s not an uncommon problem, and quite frankly- the things that you mention are very much why we built our simulator- scalable, objective role play practice and certification.  If we can talk about numbers for a moment- how many reps are currently being certified, and I know you mentioned 3 specific areas you’re certifying them in- do you have a sense for how many additional areas reps are currently certifying, along with the general cadence you require certification?\n"
    },
    {
      "role": "user",
      "content": "Hey avatar- I’m John.  Great to meet and thanks for making some time for us today, I’m excited for the chat.  If you’re alright with it, perhaps a great place to start might be to learn a bit about your interest in Quantified- and what you’re looking to solve for?"
    }
  ],
  temperature=0,
  max_tokens=950,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# print(response)

end_time = time.time()  # Record the end time
duration = end_time - start_time
print(f"Normal run completed in {duration} seconds.")

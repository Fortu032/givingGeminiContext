from google import genai
from google.genai.types import HttpOptions
import dotenv, time, sys
from utils import getContext, exportHistory, dprint, dinput

dotenv.load_dotenv()

model: str = "gemini-2.5-flash" if len(sys.argv)<2 else sys.argv[1]
client = genai.Client(http_options=HttpOptions(api_version="v1"))
chat = client.chats.create(model=model)

context, oldchat = getContext("history_1.json")
message: str = f"{context}" if not oldchat else f"{context}. Here's a chat I had with you for example: \n{oldchat}\n"
history: list = []
errors: int = 0
first: bool = True

while message != "qq":
	try:
		response = chat.send_message(message)
		if not first:
			dprint("Gemini", response.text, "green")
			history.append({
				"me": message,
				"gemini": response.text
			})
		else:
			if not oldchat:
				dprint("Context", context, "yellow")
			else:
				dprint("Context", message, "yellow")
			first = False
		message = dinput("You", "blue")
	except Exception as err:
		dprint("Error", str(err), "red")
		errors += 1
		time.sleep(2)

chatJSON = {
    "model": model,
    "errors": errors,
	"context": context,
    "history": history
}

exportHistory(chatJSON)


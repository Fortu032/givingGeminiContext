import os, json
from colorama import init, Fore, Style

init(autoreset=True)

colors: dict = {
		"red": Fore.RED,
		"yellow": Fore.YELLOW,
		"blue": Fore.BLUE,
		"green": Fore.GREEN
    }

def getContext(filepath: str = "nothing.json") -> tuple[str, str]:
	if filepath and os.path.exists(filepath):
		with open(filepath, "r", encoding="utf-8") as file:
			hist: dict = json.load(file)
			return hist["context"], hist["history"]
	return os.environ.get("DEFAULT_CONTEXT", "Hi, Google Gemini!"), ""

def exportHistory(chatJSON: dict) -> None:
	i: int = 1
	while True:
		filename: str = f"history_{i}.json"
		if not os.path.exists(filename):
			with open(filename, "w", encoding="utf-8") as file:
				json.dump(chatJSON, file, indent=4)
				break
		i += 1

def dprint(who: str, what: str, color: str) -> None:
	print(f"{colors[color.lower()]}{who}:{Style.RESET_ALL} {what}\n")
	
def dinput(who: str, color: str) -> str:
	return input(f"{colors[color.lower()]}{who}: {Style.RESET_ALL}")
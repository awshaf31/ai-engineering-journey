Greeting = input("Greeting: ").strip()
match Greeting:
    case "Hello" | "Hello, Newman" :
        print("$0")
    case "Hey" | "How you doing?" | "How it going" :
            print("$20")
    case "What's happening?" | "What's up?" :
            print("$100")

import UIKit

func getFileContent(fileName : String, fileType : String) -> String? {
	guard let path = Bundle.main.path(forResource: fileName, ofType: fileType) else {
		print("Invalid path")
		return nil
	}
	
	guard let content = try? String(contentsOfFile: path) else {
		print("File not found!")
		return nil
	}
	
	return content.trimmingCharacters(in: .whitespacesAndNewlines)
}

func isPhraseValid1(phrase : String) -> Bool {
	var isValid = true
	var wordCount = [String : Int]()
	let words = phrase.components(separatedBy: .whitespaces)
	
	for w in words {
		if wordCount[w] != nil {
			isValid = false
			break
		}
		
		wordCount[w] = 1
	}
	
	return isValid
}

func isPhraseValid2(phrase : String) -> Bool {
	var isValid = true
	var wordCount = [String : Int]()
	let words = phrase.components(separatedBy: .whitespaces)
	
	for w in words {
		let sw = w.sorted().reduce("") { (r, c) -> String in
			"\(r)\(c)"
		}
		
		if wordCount[sw] != nil {
			isValid = false
			break
		}
		
		wordCount[sw] = 1
	}
	
	return isValid
}

func numberOfValidPhrases(content : String, isValid : (String) -> Bool) -> Int {
	var num = 0
	
	let lines = content.components(separatedBy: .newlines)
	for l in lines {
		if isValid(l) {
			num += 1
		}
	}
	
	return num
}

let content = getFileContent(fileName: "input04", fileType: "txt")
let num1 = numberOfValidPhrases(content: content!, isValid: isPhraseValid1)
let num2 = numberOfValidPhrases(content: content!, isValid: isPhraseValid2)

print("Challenge 1 - number of valid phrases: \(num1)")
print("Challenge 2 - number of valid phrases: \(num2)")

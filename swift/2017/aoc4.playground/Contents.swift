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
	var appearedWords = Set<String>()
	let words = phrase.components(separatedBy: .whitespaces)
	
	for w in words {
		if appearedWords.contains(w) {
			isValid = false
			break
		}
		
		appearedWords.insert(w)
	}
	
	return isValid
}

func isPhraseValid2(phrase : String) -> Bool {
	var isValid = true
	var appearedWords = Set<String>()
	let words = phrase.components(separatedBy: .whitespaces)
	
	for w in words {
		let sw = w.sorted().reduce("") { (r, c) -> String in
			"\(r)\(c)"
		}
		
		if appearedWords.contains(sw) {
			isValid = false
			break
		}
		
		appearedWords.insert(sw)
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

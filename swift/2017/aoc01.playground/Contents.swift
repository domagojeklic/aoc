//: Playground - noun: a place where people can play

import UIKit

func sumOfMatchingDigits(input : String) -> Int {
	var sum = 0
	
	let lastIndex = input.index(before: input.endIndex)
	for index in input.indices {
		let currentDigit = input[index]
		let nextDigit = (index == lastIndex) ? input[input.startIndex] : input[input.index(after: index)]

		if currentDigit == nextDigit {
			sum += Int(String(currentDigit))!
		}
	}
	
	return sum
}

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

let input = getFileContent(fileName: "input", fileType: "txt")!
let sum = sumOfMatchingDigits(input: input)
print("Sum = \(sum)")


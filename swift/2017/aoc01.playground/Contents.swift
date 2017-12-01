//: Playground - noun: a place where people can play

import UIKit

func sumOfMatchingDigits(input : String,  offsetBy : Int) -> Int {
	var sum = 0
	
	let lastIndex = input.index(before: input.endIndex)
	var i = 0
	for index in input.indices {
		let currentDigit = input[index]
		let nextIdx = (i + offsetBy) % input.count
		let nextDigit = input[input.index(input.startIndex, offsetBy: nextIdx)]

		if currentDigit == nextDigit {
			sum += Int(String(currentDigit))!
		}
		
		i += 1
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
var sum = sumOfMatchingDigits(input: input, offsetBy: 1)
print("First challenge result = \(sum)")

let offset = input.count / 2
sum = sumOfMatchingDigits(input: input, offsetBy: offset)
print("Second challenge result = \(sum)")

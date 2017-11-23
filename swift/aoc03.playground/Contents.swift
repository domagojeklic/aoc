//: Playground - noun: a place where people can play

import UIKit

let inputFileName = "input03"
let inputFileType = "txt"

class Triangle : CustomStringConvertible {
	var a : Int = 0
	var b : Int = 0
	var c : Int = 0
	
	var description: String {
		return "(\(a), \(b), \(c))"
	}
	
	func isValid() -> Bool {
		return a < (b + c) && b < (a + c) && c < (a + b)
	}
}

func numberOfValidTriangles(inputArray : [Int]) -> Int {
	var count = 0
	let triangle = Triangle()
	
	for i in stride(from: 0, to: inputArray.count, by: 3) {
		triangle.a = inputArray[i]
		triangle.b = inputArray[i + 1]
		triangle.c = inputArray[i + 2]
		
		if (triangle.isValid()) {
			count += 1
		}
	}
	
	return count
}

func triangleSides(content : String) -> [Int] {
	let triangleSides = content.components(separatedBy: .newlines)
								.map{$0.components(separatedBy: .whitespaces)}
								.flatMap{$0}
								.filter{!$0.isEmpty}
								.map{Int($0)!}
	
	return triangleSides
}

func triangleSidesColumnBased(inputSides: [Int]) -> [Int] {
	var arr0 = [Int]()
	var arr1 = [Int]()
	var arr2 = [Int]()
	
	for i in stride(from: 0, to: inputSides.count, by: 3) {
		arr0.append(inputSides[i])
		arr1.append(inputSides[i + 1])
		arr2.append(inputSides[i + 2])
	}
	
	return arr0 + arr1 + arr2
}

func contentForFile(fileName: String, fileType: String) -> String? {
	guard let path = Bundle.main.path(forResource: fileName, ofType: fileType) else {
		print("Invalid path!")
		return nil
	}
	
	guard let content = try? String(contentsOfFile: path) else {
		print("Invalid file content!")
		return nil
	}
	
	return content
}

let content = contentForFile(fileName: inputFileName, fileType: inputFileType)
let triangleSides1 = triangleSides(content: content!)
let triangleSides2 = triangleSidesColumnBased(inputSides: triangleSides1)
let count1 = numberOfValidTriangles(inputArray: triangleSides1)
let count2 = numberOfValidTriangles(inputArray: triangleSides2)

print("First challange count: \(count1)")
print("Second challange count: \(count2)")

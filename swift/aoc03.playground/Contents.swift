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

func numberOfValidTriangles(inputFile : String, inputFileType : String) -> Int? {
	var count = 0

	guard let path = Bundle.main.path(forResource: inputFile, ofType: inputFileType) else {
		print("Invalid path!")
		return nil
	}

	guard let content = try? String(contentsOfFile: path) else {
		print("Invalid file content!")
		return nil
	}

	let lines = content.components(separatedBy: .newlines)
	var triangle = Triangle()

	for l in lines {
		let triangleLines = l.components(separatedBy: .whitespaces)
								.filter{!$0.isEmpty}
								.map{Int($0)!}

		if(triangleLines.count == 3) {
			triangle.a = triangleLines[0]
			triangle.b = triangleLines[1]
			triangle.c = triangleLines[2]

			if (triangle.isValid()) {
				count += 1
			}
		}
	}

	return count
}

let count = numberOfValidTriangles(inputFile: inputFileName, inputFileType: inputFileType)
print(count!)


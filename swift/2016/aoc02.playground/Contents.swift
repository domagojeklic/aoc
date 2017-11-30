import UIKit

var keypad1 : [[String?]] = [["1","2","3"],
							["4","5","6"],
							["7","8","9"]]
var keypad2 : [[String?]] = [[nil, nil, "1", nil, nil],
							[nil, "2", "3", "4", nil,],
							["5", "6", "7", "8", "9"],
							[nil, "A", "B", "C", nil],
							[nil, nil, "D", nil, nil]
]

let inputFileType = "txt"
let inputFile = "input02"
let inputFileTest = "input02_test"
let startRow1 = 1
let startCol1 = 1
let startRow2 = 2
let startCol2 = 0

enum Direction : String {
	case U, D, L, R
	func value() -> Int {
		switch self {
		case .D, .R:
			return 1
		case .U, .L:
			return -1
		}
	}
}

func clamp(value : Int, lower : Int, upper : Int) -> Int{
    if (value < lower) {
        return lower
    }
    else if (value > upper) {
        return upper
    }
    else {
        return value
    }
}

func calculateBathroomCode(inputFile : String, inputFileType: String, keypad : [[String?]], startRow : Int, startCol : Int) -> String? {
	var row : Int = startRow
	var col : Int = startCol
	var newRow = startRow
	var newCol = startCol
	var result = String()
	
	guard let path = Bundle.main.path(forResource: inputFile, ofType: inputFileType) else {
		print("Invalid path!")
		return nil
	}
	guard let content = try? String(contentsOfFile: path) else {
		print("File not found!")
		return nil
	}
	
	let lines = content.components(separatedBy: .newlines)
	
	for l in lines {
		if l == "" {
			continue
		}
		
		for c in l {
			let dir = Direction(rawValue: String(c))!
			
			switch dir {
			case .U, .D :
				newRow = newRow + dir.value()
				newRow = clamp(value: newRow, lower: 0, upper: keypad.count - 1)
			case .L, .R :
				newCol = newCol + dir.value()
				newCol = clamp(value: newCol, lower: 0, upper: keypad[0].count - 1)
			}
			
			if keypad[newRow][newCol] != nil {
				row = newRow
				col = newCol
			}
			else {
				newRow = row
				newCol = col
			}
		}
		result = result + String(describing:keypad[row][col]!)
	}
	
	return result
}

if let result1 = calculateBathroomCode(inputFile: inputFile, inputFileType: inputFileType, keypad: keypad1, startRow: startRow1, startCol: startCol1) {
	print("Part one result: \(result1)")
}

if let result2 = calculateBathroomCode(inputFile: inputFile, inputFileType: inputFileType, keypad: keypad2, startRow: startRow2, startCol: startCol2) {
	print("Part two result: \(result2)")
}


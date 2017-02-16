//: Playground - noun: a place where people can play

import UIKit

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

var keypad : [[Int]] = [[1,2,3],[4,5,6],[7,8,9]]
var i : Int = 1
var j : Int = 1

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

var result = ""
if let path = Bundle.main.path(forResource: "input02", ofType: "txt") {
    let content = try String(contentsOfFile: path)
    let lines = content.components(separatedBy: .newlines)
    
    for l in lines {
        if l == "" {
            continue
        }
        for c in l.characters {
            let dir = Direction(rawValue: String(c))!
            switch dir {
                case .U, .D :
                i = i + dir.value()
                i = clamp(value: i, lower: 0, upper: 2)
                case .L, .R :
                j = j + dir.value()
                j = clamp(value: j, lower: 0, upper: 2)
            }
        }
        result = result + String(keypad[i][j])
    }
    
    print(result)
}



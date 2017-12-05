import UIKit

extension Int {
    func square() -> Int {
        return self * self
    }
}

func spiralNumber(num : Int) -> Int {
    var square = Int(ceil(sqrt(Double(num))))
    if square % 2 == 0 {
        square += 1
    }
    
    return Int(ceil(Double(square) / 2))
}

func maxNumInSpiral(spiralNum : Int) -> Int {
    return (1 + (spiralNum - 1) * 2).square()
}

func manhattanDistance(spiralNum : Int, spiralIndex : Int) -> Int {
    if spiralNum == 1 {
        return 1
    }
    
    let minDistance = spiralNum - 1
    let maxDistance = 2 * minDistance
    
    var distance = maxDistance - 1
    var index = 0
    var inc = -1
    
    while index != spiralIndex {
        index += 1
        distance += inc
        
        if distance == minDistance {
            inc = 1
        }
        else if distance == maxDistance {
            inc = -1
        }
    }
    
    return distance
}

let input = 265149
let spiralNum = spiralNumber(num: input)
let maxNum = maxNumInSpiral(spiralNum: spiralNum - 1)
let spiralIndex = input - maxNum - 1

print(spiralNum)
print(spiralIndex)
print(manhattanDistance(spiralNum: spiralNum, spiralIndex: spiralIndex))


import UIKit

let input : String = "R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"

enum Direction : String {
    case L, R
    func value() -> Int {
        if self == .L {
            return -1
        }
        else {
            return 1
        }
    }
}

enum CompasDirection: Int {
    case N, E, S, W
    func count() -> Int {
        return CompasDirection.W.rawValue + 1
    }
    mutating func turn(dir : Direction) {
        var raw = (self.rawValue + dir.value()) % count()
        if raw < 0 {
            raw = count() - 1
        }
        self = CompasDirection(rawValue: raw)!
    }
}

struct Position {
    var x : Int
    var y : Int
    
    mutating func move(dir : CompasDirection, len : Int) {
        switch dir {
        case .N:
            y += len
        case .S:
            y -= len
        case .E:
            x += len
        case .W:
            x -= len
        }
    }
    
    func description() -> String {
        return "\(x), \(y)"
    }
    func distance() -> Int {
        return abs(x) + abs(y)
    }
}

struct Line {
    var p1 : Position
    var p2 : Position
    var dir : CompasDirection
}

func Intersection(line : Line, linesArray : [Line]) -> Position? {
    var p : Position? = nil
    for l in linesArray {
        if let pos = Intersection(l1: line, l2: l) {
            p = pos
            break
        }
    }
    
    return p
}

func Intersection(l1 : Line, l2 : Line) -> Position? {
    var p : Position? = nil
    if (IsBetween(a: l1.p1.x, b1: l2.p1.x, b2: l2.p2.x) &&
        IsBetween(a: l2.p1.y, b1: l1.p1.y, b2: l1.p2.y)) {
        p = Position(x: l1.p1.x, y: l2.p1.y)
    }
    if (IsBetween(a: l2.p1.x, b1: l1.p1.x, b2: l1.p2.x) &&
        IsBetween(a: l1.p1.y, b1: l2.p1.y, b2: l2.p2.y)) {
        p = Position(x: l2.p1.x, y: l1.p1.y)
    }
    return p
}

func IsBetween(a : Int, b1 : Int, b2: Int) -> Bool {
    return (b1 > a && a > b2) || (b2 > a && a > b1)
}

var currCompassDir = CompasDirection.N
var currPosition = Position(x: 0, y: 0)
var linesNS = [Line]()
var linesEW = [Line]()
let formatedInput = input.replacingOccurrences(of: " ", with: "")
let moves = formatedInput.characters.split(separator: ",").map(String.init)
var intersection : Position? = nil

for m in moves {
    let index = m.index(m.startIndex, offsetBy: 1)
    let d = m.substring(to: index)
    let l = m.substring(from: index)
    let dir = Direction(rawValue: d)!
    let oldPosition = currPosition
    
    currCompassDir.turn(dir: dir)
    currPosition.move(dir: currCompassDir, len: Int(l)!)
    
    if intersection == nil {
        let line = Line(p1: oldPosition, p2: currPosition, dir: currCompassDir)
        
        switch currCompassDir {
        case .N, .S:
            linesNS.append(line)
            intersection = Intersection(line: line, linesArray: linesEW)
        case .E, .W:
            linesEW.append(line)
            intersection = Intersection(line: line, linesArray: linesNS)
        }
    }
}

print(currPosition.description())
print(currPosition.distance())
print(intersection?.description() ?? "Intersection not found")
print(intersection?.distance() ?? "Intersection not found")


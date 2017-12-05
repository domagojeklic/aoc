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

func numStepsToExit(content : String) -> Int {
    var numSteps = 0
    var currentInstruction = 0
    var instructions = content.components(separatedBy: .newlines).map{Int($0)!}
    
    while currentInstruction >= 0 && currentInstruction < instructions.count {
        numSteps += 1
        let jump = instructions[currentInstruction]
        if jump >= 3 {
            instructions[currentInstruction] = jump - 1
        }
        else {
             instructions[currentInstruction] = jump + 1
        }
        
        currentInstruction += jump
    }
    
    return numSteps
}

let content = getFileContent(fileName: "input05", fileType: "txt")!
let numSteps = numStepsToExit(content: content)


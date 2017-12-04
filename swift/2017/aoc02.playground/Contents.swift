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

func calculateChecksum(content : String, checksumFunc : (String) -> Int) -> Int {
    var checksum = 0
    
    let rows = content.components(separatedBy: .newlines)
    for r in rows {
        checksum += checksumFunc(r)
    }
    
    return checksum
}

func checksum1(row : String) -> Int {
    let values = row.components(separatedBy: "\t").map{Int($0)!}
    let min = values.min()!
    let max = values.max()!
    
    return max - min
}

func checksum2(row : String) -> Int {
    let values = row.components(separatedBy: "\t").map{Int($0)!}
    for i in 0..<values.count - 1 {
        for j in i+1..<values.count {
            let v1 = values[i]
            let v2 = values[j]
            if v1 % v2 == 0 {
                return v1 / v2
            }
            if v2 % v1 == 0 {
                return v2 / v1
            }
        }
    }
    
    return 0
}

let content = getFileContent(fileName: "input02", fileType: "txt")!
let c1 = calculateChecksum(content: content, checksumFunc: checksum1)
print("Checksum1: \(c1)")
let c2 = calculateChecksum(content: content, checksumFunc: checksum2)
print("Checksum2: \(c2)")

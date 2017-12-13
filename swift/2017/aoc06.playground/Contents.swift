import UIKit

func redistributionBankIndex(bank : [Int]) -> Int {
    var index = 0
    var max = bank[0]
    
    for i in 1..<bank.count {
        if bank[i] > max {
            index = i
            max = bank[i]
        }
    }
    
    return index
}

func redistributeBank(bank : inout [Int], from index:Int) {
    var i = index
    var storage = bank[index]
    bank[index] = 0
    
    while storage > 0 {
        i = (i + 1) % bank.count
        bank[i] += 1
        storage -= 1
    }
}

func numOfCycles(bank : inout [Int]) -> Int {
    var num = 0
    var configurations = [String : Int]()
    repeat {
        configurations[bank.description] = num
        
        num += 1
        let index = redistributionBankIndex(bank: bank)
        redistributeBank(bank: &bank, from: index)
    } while configurations[bank.description] == nil
    
    return num - configurations[bank.description]!
}

var memoryBank = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
let numCycles = numOfCycles(bank: &memoryBank)
print("Number of cycles: \(numCycles)")

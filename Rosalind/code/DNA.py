def count_DNA(string):
  countA=string.count("A")
  countT=string.count("T")
  countG=string.count("G")
  countC=string.count("C")
  return countA, countC, countG, countT

if __name__ == "__main__":
  with open("./data/rosalind_dna.txt", "r") as f:
    string=f.readline().strip()
    countA, countC , countG, countT= count_DNA(string)
    print(countA, countC, countG, countT)
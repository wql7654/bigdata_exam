from xml.etree.ElementTree import Element, dump, SubElement

note=Element("note")
to=Element("tos") #자식 노드
to.text="Tove"
note.append(to)

SubElement(note,"from").text="Jani"
dump(note)

dummy=Element("dummy")
note.insert(1,dummy)
dump(note)
note.remove(dummy) #부모노드에 있는 자식 노드를 인자로 넘겨줘야한다.
dump(note)


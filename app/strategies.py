import json
import xml.etree.ElementTree as ET


class ConsoleDisplay:
    def display(self, content: str) -> None:
        print(content)


class ReverseDisplay:
    def display(self, content: str) -> None:
        print(content[::-1])


class ConsolePrint:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint:
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class JSONSerialize:
    def serialize(self, title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})


class XMLSerialize:
    def serialize(self, title: str, content: str) -> str:
        root = ET.Element("book")
        title_element = ET.SubElement(root, "title")
        title_element.text = title
        content_element = ET.SubElement(root, "content")
        content_element.text = content
        return ET.tostring(root, encoding="unicode")

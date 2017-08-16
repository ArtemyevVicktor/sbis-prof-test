#python 3.5.2
# -*- encoding: utf-8 -*-
#author: Artemyev Viktor
#date:06.08.2017
import sys
import os
import zipfile
from xml.etree.ElementTree import ElementTree

path = sys.argv[1]

def ZipExtract(path):
	try:
		z = zipfile.ZipFile(path, "r") 
		z.extractall()
		z.close()
	except Exception as e:
	   return False
	else:
		return True

def ZipPacked(path):
	z = zipfile.ZipFile(path, 'w')
	z.write('не совсем главный.xml')
	z.write('главный.xml')
	z.write('test/dir1')
	z.write('test/файл1.xml')
	z.close()

def TagFindAndAttribChange(FileName, Tag ):
	tree = ElementTree()
	tree.parse(FileName)
	root = tree.getroot()
	p = tree.find(Tag)
	for i in tree.findall(Tag):
		i.attrib["name"] = i.attrib["name"]+"1"
	tree.write(FileName)
	
ZipExtract(path)
#распаковываем архив
os.rename("test/dir", "test/dir1")
#директорию dir переименовать в dir1
TagFindAndAttribChange("главный.xml","tag")
#в файле "главный.xml" у всех тэгов <tag> атрибуту "name" к существующему значению дописать "1"
TagFindAndAttribChange("главный.xml","tag1")
#в файле "главный.xml" у всех тэгов <tag1> атрибуту "name" к существующему значению дописать "1"
TagFindAndAttribChange("не совсем главный.xml","tag1")
#в файле "не совсем главный.xml" у всех тэгов <tag1> атрибуту "name" к существующему значению дописать "1"
ZipPacked(path)
#упаковать в архив с тем же именем.

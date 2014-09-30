'''
Copyright (C) 2014 Jacques Lucke
mail@jlucke.com

Created by Jacques Lucke

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import bpy, random
from bpy.types import NodeTree, Node, NodeSocket
from mn_node_helper import AnimationNode
from mn_utils import *
from mn_execution import nodePropertyChanged

		
class CharactersNode(Node, AnimationNode):
	bl_idname = "CharactersNode"
	bl_label = "Characters"
	
	def init(self, context):
		self.outputs.new("StringSocket", "Lower Case")
		self.outputs.new("StringSocket", "Upper Case")
		self.outputs.new("StringSocket", "Digits")
		self.outputs.new("StringSocket", "Special")
		self.outputs.new("StringSocket", "All")
		
	def execute(self, input):
		output = {}
		output["Lower Case"] = "abcdefghijklmnopqrstuvwxyz"
		output["Upper Case"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		output["Digits"] = "0123456789"
		output["Special"] = "!§$%&/()=?*+#'-_.:,;" + '"'
		output["All"] = output["Lower Case"] + output["Upper Case"] + output["Digits"] + output["Special"]
		return output
	
		
# register
################################
		
def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)
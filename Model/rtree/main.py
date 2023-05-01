from __future__ import annotations

import ctypes
import os
import os.path
import pickle
import pprint
import sys
import warnings

import math





##!##


class Node:
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent
        self.bbox = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        self.update_bbox()
    
    def remove_child(self, child):
        self.children.remove(child)
        child.parent = None
        self.update_bbox()
    
    def merge_or_redistribute(self):
        pass  # to be implemented in subclasses
    
    def update_bbox(self):
        pass  # to be implemented in subclasses


class LeafNode(Node):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def update_bbox(self):
        if len(self.children) == 0:
            self.bbox = None

    
    def merge_or_redistribute(self):
        if self.parent is None:
            return
        siblings = self.get_siblings()
        total_children = len(self.children)
        for sibling in siblings:
            total_children += len(sibling.children)
        if total_children <= self.m:
            # merge
            for sibling in siblings:
                for child in sibling.children:
                    self.add_child(child)
                sibling.parent = None
            self.parent.remove_child(self)
            if self.parent is not None and len(self.parent.children) < self.m // 2:
                self.parent.merge_or_redistribute()
        else:
            # redistribute
            while len(self.children) < total_children // 2:
                largest_sibling = max(siblings, key=lambda s: len(s.children))
                largest_sibling.remove_child(largest_sibling.children[-1])
                self.add_child(largest_sibling.children[-1])
                siblings.remove(largest_sibling)
                total_children -= 1


class InternalNode(Node):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def update_bbox(self):
        if len(self.children) == 0:
            self.bbox = None
    
    def merge_or_redistribute(self):
        if self.parent is None:
            return
       
       
       
class RTreeNode:
    def __init__(self, is_leaf, max_entries):
        self.is_leaf = is_leaf
        self.max_entries = max_entries
        self.entries = []

class RTree:
    def __init__(self, max_entries=4):
        self.max_entries = max_entries
        self.root = RTreeNode(True, max_entries)

    def insert(self, rect, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            node.entries.append(rect)
            if len(node.entries) > node.max_entries:
                self.handle_overflow(node)
        else:
            best_child = self.choose_best_child(node, rect)
            self.insert(rect, best_child)

    def handle_overflow(self, node):
        if node == self.root:
            self.split_root()
        else:
            parent = self.find_parent(node)
            new_node = RTreeNode(node.is_leaf, node.max_entries)
            self.split(node, new_node)
            parent.entries.append(new_node)
            if len(parent.entries) > parent.max_entries:
                self.handle_overflow(parent)
 
    def split_root(self):
        old_root = self.root
        self.root = RTreeNode(False, self.max_entries)
        new_node = RTreeNode(old_root.is_leaf, old_root.max_entries)
        self.split(old_root, new_node)
        self.root.entries.append(old_root)
        self.root.entries.append(new_node)

    def split(self, node, new_node):
        node_entries = node.entries[:]
        node.entries = []
        node_entries.sort(key=lambda r: r.x1)
        left_entries = node_entries[:len(node_entries) // 2]
        right_entries = node_entries[len(node_entries) // 2:]
        node.entries = left_entries
        new_node.entries = right_entries

    def find_parent(self, node):
        if node == self.root:
            return None
        for entry in self.root.entries:
            if node in entry.entries:
                return entry
            elif not entry.is_leaf and node in entry.entries:
                return self.find_parent(entry)

    def choose_best_child(self, node, rect):
        best_child = None
        min_expansion = float('inf')
        for entry in node.entries:
            if entry.is_leaf:
                expansion = self.expansion(entry.get_rect(), rect)
                if expansion < min_expansion:
                    min_expansion = expansion
                    best_child = entry
            else:
                child_rect = entry.get_rect()
                if rect.intersects(child_rect):
                    expansion = self.expansion(child_rect, rect)
                    if expansion < min_expansion:
                        min_expansion = expansion
                        best_child = entry
        return best_child

    def expansion(self, rect1, rect2):
        return rect1.union(rect2).area - rect1.area - rect2.area


    def compute_distance(self, p1, p2):
        # p1 and p2 are tuples representing the coordinates of two points
        # Compute the Euclidean distance between the two points
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))
        return distance
    
    def nearest(self, node, point, k, heap):
        if node.is_leaf():
            for obj in node.objects:
                distance = self.compute_distance(obj, point)
                heap.push(distance, obj)
            while len(heap) > k:
                heap.pop()
        else:
            ct=0
            for child in node.children:
                distance = self.compute_distance(child.rectangle, point)
                if distance < heap.max_distance() or ct<k:
                    ct+=1
                    self.nearest(child, point, k, heap)
                    
    def delete_point(self, point):
        if self.root is None:
            return
        self.root = self._delete_point(point, self.root)
    
    def _delete_point(self, point, node):
        if isinstance(node, LeafNode):
            node.children.remove(point)
            if len(node.children) < self.m // 2:
                if node is self.root:
                    if len(node.children) == 0:
                        self.root = None
                    return node
                else:
                    parent = node.parent
                    parent.children.remove(node)
                    if len(parent.children) < self.m // 2:
                        parent.merge_or_redistribute()
                    return parent
            else:
                return node
        else:  # node is an InternalNode
            for child in node.children:
                if child.bbox.contains(point):
                    child = self._delete_point(point, child)
                    if len(child.children) < self.m // 2:
                        if child is self.root:
                            if len(child.children) == 0:
                                self.root = None
                            return child
                        else:
                            parent = child.parent
                            parent.children.remove(child)
                            if len(parent.children) < self.m // 2:
                                parent.merge_or_redistribute()
                            return parent
            return node



##!##



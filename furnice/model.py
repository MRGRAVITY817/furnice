from dataclasses import dataclass
from datetime import date
from typing import Optional

# OrderLine is immutable dataclass with no behavior.
@dataclass(frozen=True)
class OrderLine:
	order_id: str
	sku: str
	qty: int

class Batch:
	def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
		self.reference = ref
		self.sku = sku
		self.eta = eta
		self.available_quantity = qty
	
	def allocate(self, line: OrderLine):
		self.available_quantity -= line.qty
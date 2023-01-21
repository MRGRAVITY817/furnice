from furnice.model import Batch, OrderLine, allocate
from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)

def test_prefers_current_stock_batches_to_shipments():
	# Arrange
	in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
	shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
	line = OrderLine("oref", "RETRO-CLOCK", 10)
	# Act
	allocate(line, [in_stock_batch, shipment_batch])
	# Assert
	assert in_stock_batch.available_quantity == 90
	assert shipment_batch.available_quantity == 100
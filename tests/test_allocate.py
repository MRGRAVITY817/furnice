from furnice.model import Batch, OrderLine, allocate
from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)

def test_prefers_current_stock_batches_to_shipments():
	in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
	shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
	line = OrderLine("oref", "RETRO-CLOCK", 10)

	allocate(line, [in_stock_batch, shipment_batch])

	assert in_stock_batch.available_quantity == 90
	assert shipment_batch.available_quantity == 100

def test_prefers_earlier_batches():
	earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
	medium= Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
	latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
	line = OrderLine("order1",  "MINIMALIST-SPOON", 10)

	allocate(line, [earliest, medium, latest])

	assert earliest.available_quantity == 90
	assert medium.available_quantity == 100
	assert latest.available_quantity == 100
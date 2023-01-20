from furnice.model import Batch, OrderLine
from datetime import date

def make_batch_and_line(sku: str, batch_qty: int, line_qty: int): 
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )

def test_allocating_to_a_batch_reduces_the_available_quantity():
    # Arrange
    (batch, line) = make_batch_and_line("SMALL-TABLE", 20, 2)
    # Act
    batch.allocate(line)
    # Assert
    assert batch.available_quantity == 18


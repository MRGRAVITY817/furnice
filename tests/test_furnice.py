def test_allocating_to_a_batch_reduces_the_available_quantity():
    # Arrange
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE",2)
    # Act
    batch.allocate(line)
    # Assert
    assert batch.available_quantity == 18


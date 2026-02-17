#!/usr/bin/env python3
"""
Test script for Tower Builder game
Tests basic functionality without requiring a display
"""

import os
import sys

# Set up dummy drivers for headless testing
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

from tower_builder import Block, Game, BLOCK_WIDTH, BLOCK_HEIGHT, SCREEN_HEIGHT, GROUND_HEIGHT


def test_block_creation():
    """Test Block class instantiation and properties"""
    print("Testing Block creation...")
    block = Block(100, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    assert block.x == 100, "Block x position incorrect"
    assert block.y == 100, "Block y position incorrect"
    assert block.width == BLOCK_WIDTH, "Block width incorrect"
    assert block.height == BLOCK_HEIGHT, "Block height incorrect"
    assert block.velocity_y == 0, "Initial velocity should be 0"
    assert not block.is_placed, "Block should not be placed initially"
    assert not block.is_stable, "Block should not be stable initially"
    print("✓ Block creation test passed")


def test_block_physics():
    """Test block physics and gravity"""
    print("Testing Block physics...")
    block = Block(100, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    block.is_placed = True
    block.is_stable = False
    
    initial_y = block.y
    block.update([])
    
    assert block.y > initial_y, "Block should fall with gravity"
    assert block.velocity_y > 0, "Velocity should increase"
    print("✓ Block physics test passed")


def test_collision_detection():
    """Test collision detection between blocks"""
    print("Testing collision detection...")
    
    # Create two overlapping blocks
    block1 = Block(100, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    block2 = Block(110, 110, BLOCK_WIDTH, BLOCK_HEIGHT, (100, 100, 255))
    
    collision = block1.check_collision(block2)
    assert collision, "Overlapping blocks should collide"
    
    # Create two non-overlapping blocks
    block3 = Block(100, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    block4 = Block(200, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (100, 100, 255))
    
    no_collision = block3.check_collision(block4)
    assert not no_collision, "Non-overlapping blocks should not collide"
    
    print("✓ Collision detection test passed")


def test_horizontal_overlap():
    """Test horizontal overlap calculation"""
    print("Testing horizontal overlap...")
    
    block1 = Block(100, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    block2 = Block(120, 100, BLOCK_WIDTH, BLOCK_HEIGHT, (100, 100, 255))
    
    overlap = block1.get_horizontal_overlap(block2)
    assert overlap > 0, "Overlapping blocks should have positive overlap"
    assert overlap == 60, f"Expected overlap of 60, got {overlap}"
    
    print("✓ Horizontal overlap test passed")


def test_game_initialization():
    """Test Game class initialization"""
    print("Testing Game initialization...")
    game = Game()
    
    assert game.state == "MENU", "Initial state should be MENU"
    assert game.score == 0, "Initial score should be 0"
    assert game.blocks == [], "Initial blocks should be empty"
    assert game.high_score >= 0, "High score should be non-negative"
    
    print("✓ Game initialization test passed")


def test_game_reset():
    """Test game reset functionality"""
    print("Testing game reset...")
    game = Game()
    
    # Modify game state
    game.score = 100
    game.state = "PLAYING"
    
    # Reset
    game.reset_game()
    
    assert game.score == 0, "Score should reset to 0"
    assert len(game.blocks) == 0, "Blocks should be cleared"
    assert game.current_block is not None, "New block should be spawned"
    
    print("✓ Game reset test passed")


def test_block_placement():
    """Test block placement and scoring"""
    print("Testing block placement...")
    game = Game()
    game.reset_game()
    
    initial_score = game.score
    initial_blocks = len(game.blocks)
    
    if game.current_block:
        game.place_block()
        
        assert game.score > initial_score, "Score should increase"
        assert len(game.blocks) > initial_blocks, "Block count should increase"
        assert game.current_block is not None, "New block should be spawned"
    
    print("✓ Block placement test passed")


def test_tower_height():
    """Test tower height calculation"""
    print("Testing tower height calculation...")
    game = Game()
    game.reset_game()
    
    # Initially, height should be 0 (no stable blocks)
    height = game.get_tower_height()
    assert height == 0, "Initial height should be 0"
    
    # Add a stable block
    block = Block(100, SCREEN_HEIGHT - GROUND_HEIGHT - BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT, (255, 100, 100))
    block.is_stable = True
    game.blocks.append(block)
    
    height = game.get_tower_height()
    assert height > 0, "Height should be positive with stable blocks"
    
    print("✓ Tower height test passed")


def test_game_over():
    """Test game over functionality"""
    print("Testing game over...")
    game = Game()
    game.reset_game()
    game.score = 150
    
    game.game_over("Test reason")
    
    assert game.state == "GAME_OVER", "State should be GAME_OVER"
    assert game.game_over_reason == "Test reason", "Game over reason should be set"
    assert game.high_score >= 150, "High score should be updated"
    
    print("✓ Game over test passed")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Tower Builder Game Tests")
    print("=" * 60)
    print()
    
    tests = [
        test_block_creation,
        test_block_physics,
        test_collision_detection,
        test_horizontal_overlap,
        test_game_initialization,
        test_game_reset,
        test_block_placement,
        test_tower_height,
        test_game_over,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

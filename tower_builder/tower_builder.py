#!/usr/bin/env python3
"""
Tower Builder Game
A simple, fun tower-building game with physics.
"""

import pygame
import random
import sys
import json
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
DARK_GRAY = (100, 100, 100)
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (101, 67, 33)
RED = (220, 50, 50)
GREEN = (50, 220, 50)
BLUE = (50, 50, 220)
YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)

# Block colors
BLOCK_COLORS = [
    (255, 100, 100),  # Light red
    (100, 100, 255),  # Light blue
    (100, 255, 100),  # Light green
    (255, 255, 100),  # Yellow
    (255, 150, 100),  # Orange
    (200, 100, 255),  # Purple
]

# Game settings
GRAVITY = 0.5
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 40
GROUND_HEIGHT = 50
MAX_BLOCKS = 50
FALL_SPEED_LIMIT = 15


class Block:
    """Represents a single block in the tower."""
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity_y = 0
        self.is_placed = False
        self.is_stable = False
        
    def update(self, blocks):
        """Update block physics."""
        if not self.is_placed:
            return
            
        if not self.is_stable:
            # Apply gravity
            self.velocity_y += GRAVITY
            self.velocity_y = min(self.velocity_y, FALL_SPEED_LIMIT)
            self.y += self.velocity_y
            
            # Check collision with ground
            if self.y + self.height >= SCREEN_HEIGHT - GROUND_HEIGHT:
                self.y = SCREEN_HEIGHT - GROUND_HEIGHT - self.height
                self.velocity_y = 0
                self.is_stable = True
                return
            
            # Check collision with other blocks
            for other_block in blocks:
                if other_block != self and other_block.is_stable:
                    if self.check_collision(other_block):
                        # Land on top of the block
                        self.y = other_block.y - self.height
                        self.velocity_y = 0
                        
                        # Check if landing is stable (decent overlap)
                        overlap = self.get_horizontal_overlap(other_block)
                        if overlap > self.width * 0.3:  # At least 30% overlap
                            self.is_stable = True
                        else:
                            # Not stable enough, keep falling
                            self.is_stable = False
                        return
    
    def check_collision(self, other):
        """Check if this block collides with another block."""
        # Check if vertically adjacent
        if self.y + self.height > other.y and self.y < other.y + other.height:
            # Check horizontal overlap
            if self.x < other.x + other.width and self.x + self.width > other.x:
                return True
        return False
    
    def get_horizontal_overlap(self, other):
        """Calculate horizontal overlap with another block."""
        left = max(self.x, other.x)
        right = min(self.x + self.width, other.x + other.width)
        return max(0, right - left)
    
    def is_off_screen(self):
        """Check if block has fallen off the screen."""
        return self.y > SCREEN_HEIGHT + 100
    
    def draw(self, screen):
        """Draw the block on the screen."""
        # Main block
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Border
        pygame.draw.rect(screen, DARK_GRAY, (self.x, self.y, self.width, self.height), 2)
        # Highlight
        pygame.draw.rect(screen, WHITE, (self.x + 5, self.y + 5, self.width - 10, 10), 0)


class Game:
    """Main game class."""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tower Builder")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        self.font_tiny = pygame.font.Font(None, 24)
        
        # Game state
        self.state = "MENU"  # MENU, PLAYING, GAME_OVER
        self.blocks = []
        self.current_block = None
        self.score = 0
        self.high_score = self.load_high_score()
        self.game_over_reason = ""
        
    def load_high_score(self):
        """Load high score from file."""
        try:
            if os.path.exists("high_score.json"):
                with open("high_score.json", "r") as f:
                    data = json.load(f)
                    return data.get("high_score", 0)
        except:
            pass
        return 0
    
    def save_high_score(self):
        """Save high score to file."""
        try:
            with open("high_score.json", "w") as f:
                json.dump({"high_score": self.high_score}, f)
        except:
            pass
    
    def reset_game(self):
        """Reset the game to initial state."""
        self.blocks = []
        self.current_block = None
        self.score = 0
        self.game_over_reason = ""
        self.spawn_new_block()
    
    def spawn_new_block(self):
        """Spawn a new block for the player to place."""
        if len(self.blocks) >= MAX_BLOCKS:
            self.game_over("Maximum blocks reached!")
            return
        
        color = random.choice(BLOCK_COLORS)
        x = random.randint(100, SCREEN_WIDTH - BLOCK_WIDTH - 100)
        y = 50
        self.current_block = Block(x, y, BLOCK_WIDTH, BLOCK_HEIGHT, color)
    
    def place_block(self):
        """Place the current block."""
        if self.current_block:
            self.current_block.is_placed = True
            self.blocks.append(self.current_block)
            
            # Calculate score based on tower height
            tower_height = self.get_tower_height()
            base_score = 10
            height_multiplier = 1 + (tower_height // 100)
            points = base_score * height_multiplier
            self.score += points
            
            self.current_block = None
            self.spawn_new_block()
    
    def get_tower_height(self):
        """Calculate the current tower height."""
        if not self.blocks:
            return 0
        
        stable_blocks = [b for b in self.blocks if b.is_stable]
        if not stable_blocks:
            return 0
        
        highest_y = min(b.y for b in stable_blocks)
        ground_y = SCREEN_HEIGHT - GROUND_HEIGHT
        return ground_y - highest_y
    
    def game_over(self, reason):
        """End the game."""
        self.state = "GAME_OVER"
        self.game_over_reason = reason
        
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
    
    def update(self):
        """Update game logic."""
        if self.state == "PLAYING":
            # Update all blocks
            for block in self.blocks[:]:
                block.update(self.blocks)
                
                # Check if block fell off screen
                if block.is_off_screen():
                    self.blocks.remove(block)
                    self.game_over("Block fell off screen!")
                    return
            
            # Move current block left/right
            if self.current_block and not self.current_block.is_placed:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.current_block.x -= 3
                    self.current_block.x = max(0, self.current_block.x)
                if keys[pygame.K_RIGHT]:
                    self.current_block.x += 3
                    self.current_block.x = min(SCREEN_WIDTH - BLOCK_WIDTH, self.current_block.x)
    
    def draw(self):
        """Draw everything on screen."""
        # Background
        self.screen.fill(SKY_BLUE)
        
        # Ground
        pygame.draw.rect(self.screen, GROUND_COLOR, 
                        (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
        
        if self.state == "MENU":
            self.draw_menu()
        elif self.state == "PLAYING":
            self.draw_game()
        elif self.state == "GAME_OVER":
            self.draw_game_over()
        
        pygame.display.flip()
    
    def draw_menu(self):
        """Draw the main menu."""
        title = self.font_large.render("TOWER BUILDER", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title, title_rect)
        
        instructions = [
            "Build the tallest tower you can!",
            "",
            "Controls:",
            "← → : Move block left/right",
            "SPACE : Place block",
            "",
            "Press SPACE to start"
        ]
        
        y = 250
        for line in instructions:
            if line:
                text = self.font_tiny.render(line, True, BLACK)
            else:
                text = self.font_tiny.render(" ", True, BLACK)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 35
        
        # High score
        if self.high_score > 0:
            high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, YELLOW)
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 520))
            # Draw shadow
            shadow = self.font_small.render(f"High Score: {self.high_score}", True, BLACK)
            shadow_rect = shadow.get_rect(center=(SCREEN_WIDTH // 2 + 2, 522))
            self.screen.blit(shadow, shadow_rect)
            self.screen.blit(high_score_text, high_score_rect)
    
    def draw_game(self):
        """Draw the game screen."""
        # Draw all placed blocks
        for block in self.blocks:
            block.draw(self.screen)
        
        # Draw current block
        if self.current_block:
            self.current_block.draw(self.screen)
        
        # Draw score
        score_text = self.font_medium.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        # Draw tower height
        height = self.get_tower_height()
        height_text = self.font_small.render(f"Height: {int(height)}", True, BLACK)
        self.screen.blit(height_text, (10, 60))
        
        # Draw high score
        high_score_text = self.font_tiny.render(f"High: {self.high_score}", True, DARK_GRAY)
        self.screen.blit(high_score_text, (10, 100))
        
        # Draw hint
        hint_text = self.font_tiny.render("← → to move, SPACE to place", True, DARK_GRAY)
        hint_rect = hint_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))
        self.screen.blit(hint_text, hint_rect)
    
    def draw_game_over(self):
        """Draw the game over screen."""
        # Draw the game state underneath
        for block in self.blocks:
            block.draw(self.screen)
        
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Reason
        reason_text = self.font_small.render(self.game_over_reason, True, WHITE)
        reason_rect = reason_text.get_rect(center=(SCREEN_WIDTH // 2, 230))
        self.screen.blit(reason_text, reason_rect)
        
        # Score
        score_text = self.font_medium.render(f"Final Score: {self.score}", True, YELLOW)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(score_text, score_rect)
        
        # High score
        if self.score >= self.high_score:
            new_high_text = self.font_small.render("NEW HIGH SCORE!", True, GREEN)
            new_high_rect = new_high_text.get_rect(center=(SCREEN_WIDTH // 2, 360))
            self.screen.blit(new_high_text, new_high_rect)
        else:
            high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, WHITE)
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 360))
            self.screen.blit(high_score_text, high_score_rect)
        
        # Instructions
        restart_text = self.font_small.render("Press SPACE to play again", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        self.screen.blit(restart_text, restart_rect)
        
        menu_text = self.font_tiny.render("Press ESC for menu", True, LIGHT_GRAY)
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
        self.screen.blit(menu_text, menu_rect)
    
    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "GAME_OVER":
                        self.state = "MENU"
                    elif self.state == "PLAYING":
                        self.state = "MENU"
                
                if event.key == pygame.K_SPACE:
                    if self.state == "MENU":
                        self.reset_game()
                        self.state = "PLAYING"
                    elif self.state == "PLAYING":
                        if self.current_block and not self.current_block.is_placed:
                            self.place_block()
                    elif self.state == "GAME_OVER":
                        self.reset_game()
                        self.state = "PLAYING"
        
        return True
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()

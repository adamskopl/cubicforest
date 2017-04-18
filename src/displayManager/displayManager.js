import constants from './constants';
import logger from '../logger';
import { phaserInit } from '../phaser';

const log = logger.get('displayManager.js');
let game = null;

const displayManager = {
  getDisplayW: () => constants.DISPLAY_W,
  getDisplayH: () => constants.DISPLAY_H,
  loadAssets() {
    if (!game) {
      log.error('phaser not set');
      return;
    }
    game.load.spritesheet('testSpritesheet',
      'assets/testSprites.png',
      100, 100);
  },
  setGame(phaserGame) {
    game = phaserGame;
  },
};

phaserInit(displayManager);

export default displayManager;

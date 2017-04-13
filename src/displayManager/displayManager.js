import constants from './constants';
import logger from '../logger';
import { phaserInit } from '../phaser';

const log = logger.get('displayManager.js');
let phaser = null;

const displayManager = {
  getDisplayW: () => constants.DISPLAY_W,
  getDisplayH: () => constants.DISPLAY_H,
  loadAssets() {
    if (!phaser) {
      log.error('phaser not set');
      return;
    }
  },
  setGame(phaserGame) {
    phaser = phaserGame;
  },
};

phaserInit(displayManager);

export default displayManager;

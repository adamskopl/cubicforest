import logger from './logger';

const log = logger.get('phaser.js');
let displayManger = null;
let phaserGame = null;
let initialized = false;

const create = function create() {};
const preload = function preload() {
  displayManger.loadAssets();
};
const update = function update() {};
const render = function render() {};

export let phaserInit = displayM => {
  if (initialized) {
    log.warn('already initialized');
    return;
  }
  initialized = true;
  displayManger = displayM;
  phaserGame = new Phaser.Game(
    displayM.getDisplayW(),
    displayM.getDisplayH(),
    Phaser.CANVAS,
    'game', {
      preload: preload,
      create: create,
      update: update,
      render: render
    },
    null,
    false,
    false); // antialias OFF
  displayM.setGame(phaserGame);
};

export let phaser = phaserGame;

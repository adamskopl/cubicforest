import phaser from 'phaser';
import tape from 'tape';
import log from 'loglevel';

if (!phaser ||
  !tape ||
  !log) {
  console.error('imports not loaded');
}

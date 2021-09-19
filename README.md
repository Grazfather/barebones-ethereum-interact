# Barebones Ethereum dev/exploit setup

Use `brownie` for everything. Basic functionality implemented in _interact.py_.

## Basics
### To run a local chain

```bash
ganache-cli --port 8545 --gasLimit 12000000 --accounts 10 --hardfork istanbul --mnemonic brownie
```

### To deploy your contracts

```bash
brownie run interact deploy
# Or
brownie run interact deploy_attacker
brownie run interact deploy_target
```

### To query basic info from accounts

```bash
brownie run interact query
```

## Running against a real network

1. Add your `PRIVATE_KEY` to _.env_.
2. Export `WEB3_INFURA_PROJECT_ID`
3. Be careful!
4. After deploying your attacker contract, set `ATTACKER_ADDRESS` in _.env_.
5. Append `--network <network>` e.g. `--network ropsten` to your brownie
   invocation.

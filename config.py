rpcs = {
        "eth": "https://ethereum.publicnode.com",
        "zora": "https://rpc.zora.energy"
}

contracts = {
            "ZoraBridge": {
            "address": "0x1a0ad011913A150f69f6A19DF447A0CfD9551054",
            "abi": "[{\"inputs\":[{\"internalType\":\"contract L2OutputOracle\",\"name\":\"_l2Oracle\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_guardian\",\"type\":\"address\"},{\"internalType\":\"bool\",\"name\":\"_paused\",\"type\":\"bool\"},{\"internalType\":\"contract SystemConfig\",\"name\":\"_config\",\"type\":\"address\"}],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"uint8\",\"name\":\"version\",\"type\":\"uint8\"}],\"name\":\"Initialized\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"Paused\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"uint256\",\"name\":\"version\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"bytes\",\"name\":\"opaqueData\",\"type\":\"bytes\"}],\"name\":\"TransactionDeposited\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"Unpaused\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"bytes32\",\"name\":\"withdrawalHash\",\"type\":\"bytes32\"},{\"indexed\":false,\"internalType\":\"bool\",\"name\":\"success\",\"type\":\"bool\"}],\"name\":\"WithdrawalFinalized\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"bytes32\",\"name\":\"withdrawalHash\",\"type\":\"bytes32\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"}],\"name\":\"WithdrawalProven\",\"type\":\"event\"},{\"inputs\":[],\"name\":\"GUARDIAN\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"L2_ORACLE\",\"outputs\":[{\"internalType\":\"contract L2OutputOracle\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"SYSTEM_CONFIG\",\"outputs\":[{\"internalType\":\"contract SystemConfig\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_value\",\"type\":\"uint256\"},{\"internalType\":\"uint64\",\"name\":\"_gasLimit\",\"type\":\"uint64\"},{\"internalType\":\"bool\",\"name\":\"_isCreation\",\"type\":\"bool\"},{\"internalType\":\"bytes\",\"name\":\"_data\",\"type\":\"bytes\"}],\"name\":\"depositTransaction\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"donateETH\",\"outputs\":[],\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"internalType\":\"uint256\",\"name\":\"nonce\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"sender\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"target\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"gasLimit\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"internalType\":\"struct Types.WithdrawalTransaction\",\"name\":\"_tx\",\"type\":\"tuple\"}],\"name\":\"finalizeWithdrawalTransaction\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"finalizedWithdrawals\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bool\",\"name\":\"_paused\",\"type\":\"bool\"}],\"name\":\"initialize\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_l2OutputIndex\",\"type\":\"uint256\"}],\"name\":\"isOutputFinalized\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"l2Sender\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint64\",\"name\":\"_byteCount\",\"type\":\"uint64\"}],\"name\":\"minimumGasLimit\",\"outputs\":[{\"internalType\":\"uint64\",\"name\":\"\",\"type\":\"uint64\"}],\"stateMutability\":\"pure\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"params\",\"outputs\":[{\"internalType\":\"uint128\",\"name\":\"prevBaseFee\",\"type\":\"uint128\"},{\"internalType\":\"uint64\",\"name\":\"prevBoughtGas\",\"type\":\"uint64\"},{\"internalType\":\"uint64\",\"name\":\"prevBlockNum\",\"type\":\"uint64\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"pause\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"paused\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"components\":[{\"internalType\":\"uint256\",\"name\":\"nonce\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"sender\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"target\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"gasLimit\",\"type\":\"uint256\"},{\"internalType\":\"bytes\",\"name\":\"data\",\"type\":\"bytes\"}],\"internalType\":\"struct Types.WithdrawalTransaction\",\"name\":\"_tx\",\"type\":\"tuple\"},{\"internalType\":\"uint256\",\"name\":\"_l2OutputIndex\",\"type\":\"uint256\"},{\"components\":[{\"internalType\":\"bytes32\",\"name\":\"version\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"stateRoot\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"messagePasserStorageRoot\",\"type\":\"bytes32\"},{\"internalType\":\"bytes32\",\"name\":\"latestBlockhash\",\"type\":\"bytes32\"}],\"internalType\":\"struct Types.OutputRootProof\",\"name\":\"_outputRootProof\",\"type\":\"tuple\"},{\"internalType\":\"bytes[]\",\"name\":\"_withdrawalProof\",\"type\":\"bytes[]\"}],\"name\":\"proveWithdrawalTransaction\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"bytes32\",\"name\":\"\",\"type\":\"bytes32\"}],\"name\":\"provenWithdrawals\",\"outputs\":[{\"internalType\":\"bytes32\",\"name\":\"outputRoot\",\"type\":\"bytes32\"},{\"internalType\":\"uint128\",\"name\":\"timestamp\",\"type\":\"uint128\"},{\"internalType\":\"uint128\",\"name\":\"l2OutputIndex\",\"type\":\"uint128\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"unpause\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"version\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"stateMutability\":\"payable\",\"type\":\"receive\"}]"
        }
    }

nft_contract_abi = """[
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_mintFeeAmount",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "_mintFeeRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_factory",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "ADDRESS_DELEGATECALL_TO_NON_CONTRACT",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ADDRESS_LOW_LEVEL_CALL_FAILED",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "Burn_NotOwnerOrApproved",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "reason",
                "type": "bytes"
            }
        ],
        "name": "CallFailed",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalMinted",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxSupply",
                "type": "uint256"
            }
        ],
        "name": "CannotMintMoreTokens",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "mintFeeRecipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "mintFee",
                "type": "uint256"
            }
        ],
        "name": "CannotSendMintFee",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "CannotSetMintFeeToZeroAddress",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "proposedAddress",
                "type": "address"
            }
        ],
        "name": "Config_TransferHookNotSupported",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_ACCOUNTS_AND_IDS_LENGTH_MISMATCH",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_ADDRESS_ZERO_IS_NOT_A_VALID_OWNER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_BURN_AMOUNT_EXCEEDS_BALANCE",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_BURN_FROM_ZERO_ADDRESS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_CALLER_IS_NOT_TOKEN_OWNER_OR_APPROVED",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_ERC1155RECEIVER_REJECTED_TOKENS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_IDS_AND_AMOUNTS_LENGTH_MISMATCH",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_INSUFFICIENT_BALANCE_FOR_TRANSFER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_MINT_TO_ZERO_ADDRESS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_SETTING_APPROVAL_FOR_SELF",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_TRANSFER_TO_NON_ERC1155RECEIVER_IMPLEMENTER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1155_TRANSFER_TO_ZERO_ADDRESS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_NEW_IMPL_NOT_CONTRACT",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_NEW_IMPL_NOT_UUPS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_UNSUPPORTED_PROXIABLEUUID",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "ETHWithdrawFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FUNCTION_MUST_BE_CALLED_THROUGH_ACTIVE_PROXY",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FUNCTION_MUST_BE_CALLED_THROUGH_DELEGATECALL",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "contractValue",
                "type": "uint256"
            }
        ],
        "name": "FundsWithdrawInsolvent",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "INITIALIZABLE_CONTRACT_ALREADY_INITIALIZED",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "INITIALIZABLE_CONTRACT_IS_NOT_INITIALIZING",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidMintSchedule",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "mintFeeBPS",
                "type": "uint256"
            }
        ],
        "name": "MintFeeCannotBeMoreThanZeroPointOneETH",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Mint_InsolventSaleTransfer",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Mint_TokenIDMintNotAllowed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Mint_UnknownCommand",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Mint_ValueTransferFail",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "NewOwnerNeedsToBeAdmin",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "NoRendererForToken",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "renderer",
                "type": "address"
            }
        ],
        "name": "RendererNotValid",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Renderer_NotValidRendererContract",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "targetContract",
                "type": "address"
            }
        ],
        "name": "Sale_CannotCallNonSalesContract",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "expected",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "actual",
                "type": "uint256"
            }
        ],
        "name": "TokenIdMismatch",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UUPS_UPGRADEABLE_MUST_NOT_BE_CALLED_THROUGH_DELEGATECALL",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "role",
                "type": "uint256"
            }
        ],
        "name": "UserMissingRoleForToken",
        "type": "error"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "previousAdmin",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "beacon",
                "type": "address"
            }
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "updater",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "enum IZoraCreator1155.ConfigUpdate",
                "name": "updateType",
                "type": "uint8"
            },
            {
                "components": [
                    {
                        "internalType": "address",
                        "name": "owner",
                        "type": "address"
                    },
                    {
                        "internalType": "uint96",
                        "name": "__gap1",
                        "type": "uint96"
                    },
                    {
                        "internalType": "address payable",
                        "name": "fundsRecipient",
                        "type": "address"
                    },
                    {
                        "internalType": "uint96",
                        "name": "__gap2",
                        "type": "uint96"
                    },
                    {
                        "internalType": "contract ITransferHookReceiver",
                        "name": "transferHook",
                        "type": "address"
                    },
                    {
                        "internalType": "uint96",
                        "name": "__gap3",
                        "type": "uint96"
                    }
                ],
                "indexed": false,
                "internalType": "struct IZoraCreator1155TypesV1.ContractConfig",
                "name": "newConfig",
                "type": "tuple"
            }
        ],
        "name": "ConfigUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "updater",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "uri",
                "type": "string"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "name",
                "type": "string"
            }
        ],
        "name": "ContractMetadataUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "contract IRenderer1155",
                "name": "renderer",
                "type": "address"
            }
        ],
        "name": "ContractRendererUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint8",
                "name": "version",
                "type": "uint8"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "lastOwner",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "minter",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Purchased",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "renderer",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "RendererUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "newURI",
                "type": "string"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "maxSupply",
                "type": "uint256"
            }
        ],
        "name": "SetupNewToken",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "indexed": false,
                "internalType": "uint256[]",
                "name": "values",
                "type": "uint256[]"
            }
        ],
        "name": "TransferBatch",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "TransferSingle",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "string",
                "name": "value",
                "type": "string"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "URI",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "permissions",
                "type": "uint256"
            }
        ],
        "name": "UpdatedPermissions",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "indexed": false,
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "configuration",
                "type": "tuple"
            }
        ],
        "name": "UpdatedRoyalties",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "string",
                        "name": "uri",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxSupply",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalMinted",
                        "type": "uint256"
                    }
                ],
                "indexed": false,
                "internalType": "struct IZoraCreator1155TypesV1.TokenData",
                "name": "tokenData",
                "type": "tuple"
            }
        ],
        "name": "UpdatedToken",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "CONTRACT_BASE_ID",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PERMISSION_BIT_ADMIN",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PERMISSION_BIT_FUNDS_MANAGER",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PERMISSION_BIT_METADATA",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PERMISSION_BIT_MINTER",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "PERMISSION_BIT_SALES",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "permissionBits",
                "type": "uint256"
            }
        ],
        "name": "addPermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "adminMint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "tokenIds",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "quantities",
                "type": "uint256[]"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "adminMintBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "lastTokenId",
                "type": "uint256"
            }
        ],
        "name": "assumeLastTokenIdMatches",
        "outputs": [],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "accounts",
                "type": "address[]"
            },
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            }
        ],
        "name": "balanceOfBatch",
        "outputs": [
            {
                "internalType": "uint256[]",
                "name": "batchBalances",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "tokenIds",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "name": "burnBatch",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "callRenderer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "contract IMinter1155",
                "name": "salesConfig",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "callSale",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "config",
        "outputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "uint96",
                "name": "__gap1",
                "type": "uint96"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "internalType": "uint96",
                "name": "__gap2",
                "type": "uint96"
            },
            {
                "internalType": "contract ITransferHookReceiver",
                "name": "transferHook",
                "type": "address"
            },
            {
                "internalType": "uint96",
                "name": "__gap3",
                "type": "uint96"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractVersion",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "customRenderers",
        "outputs": [
            {
                "internalType": "contract IRenderer1155",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getCustomRenderer",
        "outputs": [
            {
                "internalType": "contract IRenderer1155",
                "name": "customRenderer",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "getPermissions",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getRoyalties",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getTokenInfo",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "string",
                        "name": "uri",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxSupply",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalMinted",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IZoraCreator1155TypesV1.TokenData",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "contractName",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "newContractURI",
                "type": "string"
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "defaultRoyaltyConfiguration",
                "type": "tuple"
            },
            {
                "internalType": "address payable",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "bytes[]",
                "name": "setupActions",
                "type": "bytes[]"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "role",
                "type": "uint256"
            }
        ],
        "name": "isAdminOrRole",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "metadataRendererContract",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IMinter1155",
                "name": "minter",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "minterArguments",
                "type": "bytes"
            }
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mintFee",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "mintFeeRecipient",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes[]",
                "name": "data",
                "type": "bytes[]"
            }
        ],
        "name": "multicall",
        "outputs": [
            {
                "internalType": "bytes[]",
                "name": "results",
                "type": "bytes[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "nextTokenId",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "permissions",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "permissionBits",
                "type": "uint256"
            }
        ],
        "name": "removePermission",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "royalties",
        "outputs": [
            {
                "internalType": "uint32",
                "name": "royaltyMintSchedule",
                "type": "uint32"
            },
            {
                "internalType": "uint32",
                "name": "royaltyBPS",
                "type": "uint32"
            },
            {
                "internalType": "address",
                "name": "royaltyRecipient",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "salePrice",
                "type": "uint256"
            }
        ],
        "name": "royaltyInfo",
        "outputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "royaltyAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256[]",
                "name": "ids",
                "type": "uint256[]"
            },
            {
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeBatchTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "id",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            }
        ],
        "name": "setFundsRecipient",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "setOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "contract IRenderer1155",
                "name": "renderer",
                "type": "address"
            }
        ],
        "name": "setTokenMetadataRenderer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract ITransferHookReceiver",
                "name": "transferHook",
                "type": "address"
            }
        ],
        "name": "setTransferHook",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "newURI",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "maxSupply",
                "type": "uint256"
            }
        ],
        "name": "setupNewToken",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "totalSupply",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "mintAmount",
                "type": "uint256"
            }
        ],
        "name": "supplyRoyaltyInfo",
        "outputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "royaltyAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_newURI",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_newName",
                "type": "string"
            }
        ],
        "name": "updateContractMetadata",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "newConfiguration",
                "type": "tuple"
            }
        ],
        "name": "updateRoyaltiesForToken",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_newURI",
                "type": "string"
            }
        ],
        "name": "updateTokenURI",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "uri",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
    ]"""

nft_ZoraCreator_contract_abi = """
[
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_zoraERC721TransferHelper",
                "type": "address"
            },
            {
                "internalType": "contract IFactoryUpgradeGate",
                "name": "_factoryUpgradeGate",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_marketFilterDAOAddress",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_mintFeeAmount",
                "type": "uint256"
            },
            {
                "internalType": "address payable",
                "name": "_mintFeeRecipient",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            }
        ],
        "name": "Access_MissingRoleOrAdmin",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Access_OnlyAdmin",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Access_WithdrawNotAllowed",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "proposedAddress",
                "type": "address"
            }
        ],
        "name": "Admin_InvalidUpgradeAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Admin_UnableToFinalizeNotOpenEdition",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ApprovalCallerNotOwnerNorApproved",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ApprovalQueryForNonexistentToken",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ApprovalToCurrentOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ApproveToCaller",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "BalanceQueryForZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ExternalMetadataRenderer_CallFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "InvalidMintSchedule",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "MarketFilterDAOAddressNotSupportedForChain",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "MintFee_FundsSendFailure",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "MintToZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "MintZeroQuantity",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Mint_SoldOut",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ONLY_OWNER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ONLY_PENDING_OWNER",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "OperatorNotAllowed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "OwnerQueryForNonexistentToken",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Presale_Inactive",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Presale_MerkleNotApproved",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Presale_TooManyForAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Purchase_TooManyForAddress",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "correctPrice",
                "type": "uint256"
            }
        ],
        "name": "Purchase_WrongPrice",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "RemoteOperatorFilterRegistryCallFailed",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Sale_Inactive",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "uint16",
                "name": "maxRoyaltyBPS",
                "type": "uint16"
            }
        ],
        "name": "Setup_RoyaltyPercentageTooHigh",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferCallerNotOwnerNorApproved",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferFromIncorrectOwner",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToNonERC721ReceiverImplementer",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "TransferToZeroAddress",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "URIQueryForNonexistentToken",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Withdraw_FundsSendFailure",
        "type": "error"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "previousAdmin",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "approved",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "ApprovalForAll",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "_fromTokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "_toTokenId",
                "type": "uint256"
            }
        ],
        "name": "BatchMetadataUpdate",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "beacon",
                "type": "address"
            }
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "source",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "FundsReceived",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newAddress",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "changedBy",
                "type": "address"
            }
        ],
        "name": "FundsRecipientChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "withdrawnBy",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "withdrawnTo",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "feeRecipient",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "feeAmount",
                "type": "uint256"
            }
        ],
        "name": "FundsWithdrawn",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "_tokenId",
                "type": "uint256"
            }
        ],
        "name": "MetadataUpdate",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "tokenContract",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "comment",
                "type": "string"
            }
        ],
        "name": "MintComment",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "mintFeeAmount",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "mintFeeRecipient",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "bool",
                "name": "success",
                "type": "bool"
            }
        ],
        "name": "MintFeePayout",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "numberOfMints",
                "type": "uint256"
            }
        ],
        "name": "OpenMintFinalized",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "potentialNewOwner",
                "type": "address"
            }
        ],
        "name": "OwnerCanceled",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "potentialNewOwner",
                "type": "address"
            }
        ],
        "name": "OwnerPending",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "previousAdminRole",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "newAdminRole",
                "type": "bytes32"
            }
        ],
        "name": "RoleAdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "RoleGranted",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
        ],
        "name": "RoleRevoked",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "pricePerToken",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "firstPurchasedTokenId",
                "type": "uint256"
            }
        ],
        "name": "Sale",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "changedBy",
                "type": "address"
            }
        ],
        "name": "SalesConfigChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "contract IMetadataRenderer",
                "name": "renderer",
                "type": "address"
            }
        ],
        "name": "UpdatedMetadataRenderer",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "DEFAULT_ADMIN_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MINTER_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "SALES_MANAGER_ROLE",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            }
        ],
        "name": "adminMint",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "recipients",
                "type": "address[]"
            }
        ],
        "name": "adminMintAirdrop",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "callMetadataRenderer",
        "outputs": [
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "config",
        "outputs": [
            {
                "internalType": "contract IMetadataRenderer",
                "name": "metadataRenderer",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractVersion",
        "outputs": [
            {
                "internalType": "uint32",
                "name": "",
                "type": "uint32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "factoryUpgradeGate",
        "outputs": [
            {
                "internalType": "contract IFactoryUpgradeGate",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "finalizeOpenEdition",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "getApproved",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            }
        ],
        "name": "getRoleAdmin",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "grantRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "hasRole",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_contractName",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_contractSymbol",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "_initialOwner",
                "type": "address"
            },
            {
                "internalType": "address payable",
                "name": "_fundsRecipient",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "_editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "_royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "bytes[]",
                "name": "_setupCalls",
                "type": "bytes[]"
            },
            {
                "internalType": "contract IMetadataRenderer",
                "name": "_metadataRenderer",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "_metadataRendererInit",
                "type": "bytes"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "user",
                "type": "address"
            }
        ],
        "name": "isAdmin",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "nftOwner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            }
        ],
        "name": "isApprovedForAll",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bool",
                "name": "enable",
                "type": "bool"
            }
        ],
        "name": "manageMarketFilterDAOSubscription",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "marketFilterDAOAddress",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "metadataRenderer",
        "outputs": [
            {
                "internalType": "contract IMetadataRenderer",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "minter",
                "type": "address"
            }
        ],
        "name": "mintedPerAddress",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "uint256",
                        "name": "totalMints",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "presaleMints",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "publicMints",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IERC721Drop.AddressMintDetails",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes[]",
                "name": "data",
                "type": "bytes[]"
            }
        ],
        "name": "multicall",
        "outputs": [
            {
                "internalType": "bytes[]",
                "name": "results",
                "type": "bytes[]"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "ownerOf",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "presaleMintsByAddress",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            }
        ],
        "name": "purchase",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxQuantity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "pricePerToken",
                "type": "uint256"
            },
            {
                "internalType": "bytes32[]",
                "name": "merkleProof",
                "type": "bytes32[]"
            }
        ],
        "name": "purchasePresale",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "maxQuantity",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "pricePerToken",
                "type": "uint256"
            },
            {
                "internalType": "bytes32[]",
                "name": "merkleProof",
                "type": "bytes32[]"
            },
            {
                "internalType": "string",
                "name": "comment",
                "type": "string"
            }
        ],
        "name": "purchasePresaleWithComment",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "comment",
                "type": "string"
            }
        ],
        "name": "purchaseWithComment",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "comment",
                "type": "string"
            }
        ],
        "name": "purchaseWithRecipient",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "renounceRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "revokeRole",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "_salePrice",
                "type": "uint256"
            }
        ],
        "name": "royaltyInfo",
        "outputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "royaltyAmount",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "royaltyMintSchedule",
        "outputs": [
            {
                "internalType": "uint32",
                "name": "",
                "type": "uint32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "_data",
                "type": "bytes"
            }
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "saleDetails",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "bool",
                        "name": "publicSaleActive",
                        "type": "bool"
                    },
                    {
                        "internalType": "bool",
                        "name": "presaleActive",
                        "type": "bool"
                    },
                    {
                        "internalType": "uint256",
                        "name": "publicSalePrice",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "totalMinted",
                        "type": "uint256"
                    },
                    {
                        "internalType": "uint256",
                        "name": "maxSupply",
                        "type": "uint256"
                    }
                ],
                "internalType": "struct IERC721Drop.SaleDetails",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "salesConfig",
        "outputs": [
            {
                "internalType": "uint104",
                "name": "publicSalePrice",
                "type": "uint104"
            },
            {
                "internalType": "uint32",
                "name": "maxSalePurchasePerAddress",
                "type": "uint32"
            },
            {
                "internalType": "uint64",
                "name": "publicSaleStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "publicSaleEnd",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "presaleStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "presaleEnd",
                "type": "uint64"
            },
            {
                "internalType": "bytes32",
                "name": "presaleMerkleRoot",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "operator",
                "type": "address"
            },
            {
                "internalType": "bool",
                "name": "approved",
                "type": "bool"
            }
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address payable",
                "name": "newRecipientAddress",
                "type": "address"
            }
        ],
        "name": "setFundsRecipient",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "contract IMetadataRenderer",
                "name": "newRenderer",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "setupRenderer",
                "type": "bytes"
            }
        ],
        "name": "setMetadataRenderer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "setOwner",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint104",
                "name": "publicSalePrice",
                "type": "uint104"
            },
            {
                "internalType": "uint32",
                "name": "maxSalePurchasePerAddress",
                "type": "uint32"
            },
            {
                "internalType": "uint64",
                "name": "publicSaleStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "publicSaleEnd",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "presaleStart",
                "type": "uint64"
            },
            {
                "internalType": "uint64",
                "name": "presaleEnd",
                "type": "uint64"
            },
            {
                "internalType": "bytes32",
                "name": "presaleMerkleRoot",
                "type": "bytes32"
            }
        ],
        "name": "setSaleConfiguration",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
        ],
        "name": "supportsInterface",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "tokenURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "bytes",
                "name": "args",
                "type": "bytes"
            }
        ],
        "name": "updateMarketFilterSettings",
        "outputs": [
            {
                "internalType": "bytes",
                "name": "",
                "type": "bytes"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint32",
                "name": "newSchedule",
                "type": "uint32"
            }
        ],
        "name": "updateRoyaltyMintSchedule",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "withdraw",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "zoraERC721TransferHelper",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "quantity",
                "type": "uint256"
            }
        ],
        "name": "zoraFeeForAmount",
        "outputs": [
            {
                "internalType": "address payable",
                "name": "recipient",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "fee",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "stateMutability": "payable",
        "type": "receive"
    }
]
"""

ZoraCreator1155Factory_contract_abi = """
[
    {
        "inputs": [
            {
                "internalType": "contract IZoraCreator1155",
                "name": "_implementation",
                "type": "address"
            },
            {
                "internalType": "contract IMinter1155",
                "name": "_merkleMinter",
                "type": "address"
            },
            {
                "internalType": "contract IMinter1155",
                "name": "_fixedPriceMinter",
                "type": "address"
            },
            {
                "internalType": "contract IMinter1155",
                "name": "_redeemMinterFactory",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "ADDRESS_DELEGATECALL_TO_NON_CONTRACT",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ADDRESS_LOW_LEVEL_CALL_FAILED",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "Constructor_ImplCannotBeZero",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_NEW_IMPL_NOT_CONTRACT",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_NEW_IMPL_NOT_UUPS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ERC1967_UNSUPPORTED_PROXIABLEUUID",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FUNCTION_MUST_BE_CALLED_THROUGH_ACTIVE_PROXY",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "FUNCTION_MUST_BE_CALLED_THROUGH_DELEGATECALL",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "INITIALIZABLE_CONTRACT_ALREADY_INITIALIZED",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "INITIALIZABLE_CONTRACT_IS_NOT_INITIALIZING",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ONLY_OWNER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "ONLY_PENDING_OWNER",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "OWNER_CANNOT_BE_ZERO_ADDRESS",
        "type": "error"
    },
    {
        "inputs": [],
        "name": "UUPS_UPGRADEABLE_MUST_NOT_BE_CALLED_THROUGH_DELEGATECALL",
        "type": "error"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "expected",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "actual",
                "type": "string"
            }
        ],
        "name": "UpgradeToMismatchedContractName",
        "type": "error"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "previousAdmin",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "beacon",
                "type": "address"
            }
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [],
        "name": "FactorySetup",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "uint8",
                "name": "version",
                "type": "uint8"
            }
        ],
        "name": "Initialized",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "canceledOwner",
                "type": "address"
            }
        ],
        "name": "OwnerCanceled",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "pendingOwner",
                "type": "address"
            }
        ],
        "name": "OwnerPending",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "prevOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnerUpdated",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "newContract",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "creator",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "contractURI",
                "type": "string"
            },
            {
                "indexed": false,
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "indexed": false,
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "defaultRoyaltyConfiguration",
                "type": "tuple"
            }
        ],
        "name": "SetupNewContract",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "baseImpl",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "upgradeImpl",
                "type": "address"
            }
        ],
        "name": "UpgradeRegistered",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "baseImpl",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "upgradeImpl",
                "type": "address"
            }
        ],
        "name": "UpgradeRemoved",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "acceptOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "cancelOwnershipTransfer",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractName",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractVersion",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "newContractURI",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "components": [
                    {
                        "internalType": "uint32",
                        "name": "royaltyMintSchedule",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint32",
                        "name": "royaltyBPS",
                        "type": "uint32"
                    },
                    {
                        "internalType": "address",
                        "name": "royaltyRecipient",
                        "type": "address"
                    }
                ],
                "internalType": "struct ICreatorRoyaltiesControl.RoyaltyConfiguration",
                "name": "defaultRoyaltyConfiguration",
                "type": "tuple"
            },
            {
                "internalType": "address payable",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "bytes[]",
                "name": "setupActions",
                "type": "bytes[]"
            }
        ],
        "name": "createContract",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "defaultMinters",
        "outputs": [
            {
                "internalType": "contract IMinter1155[]",
                "name": "minters",
                "type": "address[]"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "fixedPriceMinter",
        "outputs": [
            {
                "internalType": "contract IMinter1155",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "implementation",
        "outputs": [
            {
                "internalType": "contract IZoraCreator1155",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_initialOwner",
                "type": "address"
            }
        ],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "name": "isAllowedUpgrade",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "baseImpl",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "upgradeImpl",
                "type": "address"
            }
        ],
        "name": "isRegisteredUpgradePath",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "merkleMinter",
        "outputs": [
            {
                "internalType": "contract IMinter1155",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "pendingOwner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "redeemMinterFactory",
        "outputs": [
            {
                "internalType": "contract IMinter1155",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address[]",
                "name": "baseImpls",
                "type": "address[]"
            },
            {
                "internalType": "address",
                "name": "upgradeImpl",
                "type": "address"
            }
        ],
        "name": "registerUpgradePath",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "baseImpl",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "upgradeImpl",
                "type": "address"
            }
        ],
        "name": "removeUpgradePath",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "resignOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_newOwner",
                "type": "address"
            }
        ],
        "name": "safeTransferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
"""

ZoraNFTCreator_contract_abi= """
[
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_implementation",
                "type": "address"
            },
            {
                "internalType": "contract EditionMetadataRenderer",
                "name": "_editionMetadataRenderer",
                "type": "address"
            },
            {
                "internalType": "contract DropMetadataRenderer",
                "name": "_dropMetadataRenderer",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "previousAdmin",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "address",
                "name": "newAdmin",
                "type": "address"
            }
        ],
        "name": "AdminChanged",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "beacon",
                "type": "address"
            }
        ],
        "name": "BeaconUpgraded",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "creator",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "editionContractAddress",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "editionSize",
                "type": "uint256"
            }
        ],
        "name": "CreatedDrop",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "implementation",
                "type": "address"
            }
        ],
        "name": "Upgraded",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "contractName",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractURI",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "contractVersion",
        "outputs": [
            {
                "internalType": "uint32",
                "name": "",
                "type": "uint32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "internalType": "bytes[]",
                "name": "setupCalls",
                "type": "bytes[]"
            },
            {
                "internalType": "contract IMetadataRenderer",
                "name": "metadataRenderer",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "metadataInitializer",
                "type": "bytes"
            },
            {
                "internalType": "address",
                "name": "createReferral",
                "type": "address"
            }
        ],
        "name": "createAndConfigureDrop",
        "outputs": [
            {
                "internalType": "address payable",
                "name": "newDropAddress",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint104",
                        "name": "publicSalePrice",
                        "type": "uint104"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct IERC721Drop.SalesConfiguration",
                "name": "saleConfig",
                "type": "tuple"
            },
            {
                "internalType": "string",
                "name": "metadataURIBase",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "metadataContractURI",
                "type": "string"
            }
        ],
        "name": "createDrop",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint104",
                        "name": "publicSalePrice",
                        "type": "uint104"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct IERC721Drop.SalesConfiguration",
                "name": "saleConfig",
                "type": "tuple"
            },
            {
                "internalType": "string",
                "name": "metadataURIBase",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "metadataContractURI",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "createReferral",
                "type": "address"
            }
        ],
        "name": "createDropWithReferral",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint104",
                        "name": "publicSalePrice",
                        "type": "uint104"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct IERC721Drop.SalesConfiguration",
                "name": "saleConfig",
                "type": "tuple"
            },
            {
                "internalType": "string",
                "name": "description",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "animationURI",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "imageURI",
                "type": "string"
            }
        ],
        "name": "createEdition",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint104",
                        "name": "publicSalePrice",
                        "type": "uint104"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct IERC721Drop.SalesConfiguration",
                "name": "saleConfig",
                "type": "tuple"
            },
            {
                "internalType": "string",
                "name": "description",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "animationURI",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "imageURI",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "createReferral",
                "type": "address"
            }
        ],
        "name": "createEditionWithReferral",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "dropMetadataRenderer",
        "outputs": [
            {
                "internalType": "contract DropMetadataRenderer",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "editionMetadataRenderer",
        "outputs": [
            {
                "internalType": "contract EditionMetadataRenderer",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "implementation",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "initialize",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "proxiableUUID",
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol",
                "type": "string"
            },
            {
                "internalType": "address",
                "name": "defaultAdmin",
                "type": "address"
            },
            {
                "internalType": "uint64",
                "name": "editionSize",
                "type": "uint64"
            },
            {
                "internalType": "uint16",
                "name": "royaltyBPS",
                "type": "uint16"
            },
            {
                "internalType": "address payable",
                "name": "fundsRecipient",
                "type": "address"
            },
            {
                "components": [
                    {
                        "internalType": "uint104",
                        "name": "publicSalePrice",
                        "type": "uint104"
                    },
                    {
                        "internalType": "uint32",
                        "name": "maxSalePurchasePerAddress",
                        "type": "uint32"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "publicSaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleStart",
                        "type": "uint64"
                    },
                    {
                        "internalType": "uint64",
                        "name": "presaleEnd",
                        "type": "uint64"
                    },
                    {
                        "internalType": "bytes32",
                        "name": "presaleMerkleRoot",
                        "type": "bytes32"
                    }
                ],
                "internalType": "struct IERC721Drop.SalesConfiguration",
                "name": "saleConfig",
                "type": "tuple"
            },
            {
                "internalType": "contract IMetadataRenderer",
                "name": "metadataRenderer",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "metadataInitializer",
                "type": "bytes"
            },
            {
                "internalType": "address",
                "name": "createReferral",
                "type": "address"
            }
        ],
        "name": "setupDropsContract",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            }
        ],
        "name": "upgradeTo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newImplementation",
                "type": "address"
            },
            {
                "internalType": "bytes",
                "name": "data",
                "type": "bytes"
            }
        ],
        "name": "upgradeToAndCall",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]"""

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EliteNagGang is ERC721, Ownable {
    mapping(uint => address) public collectsOwner;
    mapping(address => uint) public collectsOwnerById;
    uint256 private _reserved = 100;
    uint256 private _price = 0.05 ether;
    bool private _paused = true;
    uint256 private _counterCollect = 0;

    address t1_34 = 0x13F58543FD794C88221cc75f23e72541027aA3BD;
    address t2_34 = 0x9dD990f772b482C8e984936408514c032D85d47C;
    address t3_29 = 0x13F58543FD794C88221cc75f23e72541027aA3BD;
    address t4_3 = 0x13F58543FD794C88221cc75f23e72541027aA3BD;

    constructor(string memory baseURI, address _VRFCoordinator, address _LinkToken, bytes32 _keyhash)
    public
    ERC721("Elite Nag Gang", "ELITENAGGANG")  {
        setBaseURI(baseURI);
    }

    function addCounterCollect(uint num) private {
        _counterCollect += num;
    }

    function getCounterCollect() public view returns(uint256){
        return _counterCollect;
    }

    function setPrice(uint256 _newPrice) public onlyOwner {
        _price = _newPrice;
    }

    function getPrice() public view returns (uint256){
        return _price;
    }

    function setBaseURI(string memory baseURI) public onlyOwner {
        _setBaseURI(baseURI);
    }

    function createCollectible() public onlyOwner returns(uint256) {
        uint256 tokenId = getCounterCollect();
        _safeMint(msg.sender, getCounterCollect());
        addCounterCollect(1);
        return tokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }

    function pause(bool val) public onlyOwner {
        _paused = val;
    }

    function adopt(uint256 num) public payable {
        uint256 supply = totalSupply();
        require( !_paused,                              "Sale paused" );
        require( num < 21,                              "You can adopt a maximum of 20 Nags" );
        require( supply + num < 10000 - _reserved,      "Exceeds maximum Nags supply" );
        require( msg.value >= _price * num,             "Ether sent is not correct" );
        
        for(uint256 i = 0; i < num; i++) {
            //радомное не повторяющиеся значение от 0 до 10000
            uint randoTokenId = 0;
            _safeMint( msg.sender, randoTokenId);
            // approve(to, tokenId);
            // safeTransferFrom(from, to, randoTokenId);
        }
    }

    function withdrawAll() public payable onlyOwner {
        uint256 one_percent = address(this).balance / 100;
        require(payable(t1_34).send(one_percent * 34));
        require(payable(t2_34).send(one_percent * 34));
        require(payable(t3_29).send(one_percent * 29));
        require(payable(t4_3).send(one_percent * 3));
    }
}

# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def test__item__quantity__never_drops_below_zero():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 0 <= items[0].quality

def test__item__quality__decreases_with_age():
    ...

def test__aged_brie__quality__increases_with_age():
    ...

@pytest.mark.parametrize('days_left, quality, expected_quality', [
    pytest.param(12, 10, 11, id='upgrade by one with more than 10 days'),
    pytest.param(8, 10, 11, id='upgrade by two with less then 10 days', marks=pytest.mark.xfail),
])
def test__backstage_tickets__quality__changes_as_specified(days_left, quality, expected_quality):
    """This test tests backstage passes at various times in its lifecycle. The parameters are provided by the parametrized function above."""

    # GIVEN backstage tickets...
    items = [Item("Backstage passes to a TAFKAL80ETC concert", days_left, quality)]
    gilded_rose = GildedRose(items)

    # WHEN we update the quantity
    gilded_rose.update_quality()

    # THEN the quantity is as expected
    assert expected_quality == items[0].quality

def test__backstage_tickets__quality__increases_by_two_with_less_than_10_days():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 12 == items[0].quality

def test__legendary__quality__never_decreases():
    ...

def test__legendary__quality__always_80():
    ...
    items = [Item("Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert 80 == items[0].quality


@pytest.mark.xfail(reason='This is the way it should work', strict=True)
def test__legendary__quality__always_80():
    assert True
